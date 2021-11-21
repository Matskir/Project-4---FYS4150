#include <random>
#include <chrono>
#include <iostream>
#include <armadillo>

using namespace std;

//Inline function for periodic boundary conditions using modulus
inline int periodic(int i, int limit, int add){
  return (i+limit+add)%(limit);
}


//Function that initialises energy, spin matrix and magnetisation
void initialise(int L, arma::mat& spin_matrix, double& E, double& M){
  unsigned int seed = chrono::system_clock::now().time_since_epoch().count();

  uniform_int_distribution<int> my_01_pdf(0,1);
  mt19937 generator;
  generator.seed(seed);

  //setup spin matrix and initial magnetisation/energy
  for (int y=0; y<L; y++){
    for (int x=0; x<L; x++){
      int rand_num = my_01_pdf(generator);
      if (rand_num==0){
        spin_matrix(y,x) = -1;
      }

      else{
        spin_matrix(y,x) = rand_num;
      }
    }
  }

  for (int y=0; y<L; y++){
    for (int x=0; x<L; x++){
      M += (double) spin_matrix(y,x);
      E -= (double) spin_matrix(y,x)*(spin_matrix(periodic(y,L,-1),x)
                                     + spin_matrix(y,periodic(x,L,-1)));
    }
  }
}

void initialise_ordered(int L, arma::mat& spin_matrix, double& E, double& M, int direction){
  if (direction==1) spin_matrix = arma::mat(L,L).fill(1.);
  if (direction==-1) spin_matrix = arma::mat(L,L).fill(-1.);

  for (int y=0; y<L; y++){
    for (int x=0; x<L; x++){
      M += (double) spin_matrix(y,x);
      E -= (double) spin_matrix(y,x)*(spin_matrix(periodic(y,L,-1),x)
                                     + spin_matrix(y,periodic(x,L,-1)));
    }
  }
}


void Metropolis(int L, arma::mat& spin_matrix, double& E, double& M, double *w){
  unsigned int seed = chrono::system_clock::now().time_since_epoch().count();

  uniform_real_distribution<double> my_01_real_pdf(0,1);
  uniform_int_distribution<int> my_L_pdf(0,L-1);
  mt19937 generator;
  generator.seed(seed);

  //Loop over all spins
  for (int y=0; y<L; y++){
    for (int x=0; x<L; x++){

      //Find random position
      int ix = my_L_pdf(generator);
      int iy = my_L_pdf(generator);
      int deltaE = 2*spin_matrix(iy,ix)*(spin_matrix(iy,periodic(ix,L,-1))
                      +  spin_matrix(periodic(iy,L,-1),ix)
                      +  spin_matrix(iy,periodic(ix,L,1))
                      +  spin_matrix(periodic(iy,L,1),ix));

      //Here we perform the Metropolis test
      if (my_01_real_pdf(generator) <= w[deltaE+8]){

        //Flip one spin and accept new spin configuration
        spin_matrix(iy,ix) *= -1;

        //Update energy and magnetisation
        M += (double) 2*spin_matrix(iy,ix);
        E += (double) deltaE;
      }
    }
  }
}

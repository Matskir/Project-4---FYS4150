#include "important_functions.hpp"

//Program used to generate epsilon samples to make normalised histograms to estimate full probability distribution

int main(){
  // initialise variables
  double E = 0;
  double M = 0;
  double temp = 2.4;
  int L = 20;
  double w[17], average[5];

  // setup array for possible energy changes
  for( int de =-8; de <= 8; de++) w[de+8] = 0;
  for( int de =-8; de <= 8; de+=4) w[de+8] = exp(-de/temp);

  // initialise array for expectation values
  for( int i = 0; i < 5; i++) average[i] = 0.;

  // initialise spin matrix
  arma::mat spin_matrix = arma::mat(L,L);
  initialise(L,spin_matrix,E,M);

  // set up a output file
  std::ofstream myfile_eps;
  myfile_eps.open ("output_eps_histo_T2.txt");

  // number of Monte Carlo cycles
  int mcs = 20000;

  // for loop that runs over all MC cycles
  for (int cycles = 1; cycles <= mcs; cycles++){
    Metropolis(L, spin_matrix, E, M, w);

    // update expectation values
    average[0] += E; average[1] += E*E;
    average[2] += M*M; average[3] += fabs(M);

    // write to file
    myfile_eps << cycles << "    " << E/L/L << endl;
  }

  // close the output file
  myfile_eps.close();

  return 0;
}

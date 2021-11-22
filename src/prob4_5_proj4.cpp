#include "important_functions.hpp"

//Program used to generate e,e^2,|m|,m^2 samples to make plot these over Monte Carlo cycles
//Used to solve Problem 4 and Problem 5. To generate samples for Problem 5 change L to 20

int main(){
  // initialise variables
  double E = 0;
  double M = 0;
  double temp = 1;
  int L = 2;
  //int L = 20;
  double w[17], average[5];

  // setup array for possible energy changes
  for( int de =-8; de <= 8; de++) w[de+8] = 0;
  for( int de =-8; de <= 8; de+=4) w[de+8] = exp(-de/temp);

  // initialise array for expectation values
  for( int i = 0; i < 5; i++) average[i] = 0.;

  // initialise spin matrix
  arma::mat spin_matrix = arma::mat(L,L);
  initialise(L,spin_matrix,E,M);

  // set up output files
  std::ofstream myfile_eps;
  std::ofstream myfile_eps2;
  std::ofstream myfile_mag;
  std::ofstream myfile_mag2;

  myfile_eps.open ("output_eps.txt");
  myfile_eps2.open ("output_eps2.txt");
  myfile_mag.open ("output_mag.txt");
  myfile_mag2.open ("output_mag2.txt");

  // number of Monte Carlo cycles
  int mcs = 20000;

  // for loop that runs over all MC cycles
  for (int cycles = 1; cycles <= mcs; cycles++){
    Metropolis(L, spin_matrix, E, M, w);

    // update expectation values
    average[0] += E; average[1] += E*E;
    average[2] += M*M; average[3] += fabs(M);

    // write to file
    myfile_eps << cycles << "    " << average[0]/cycles/L/L << endl;
    myfile_eps2 << cycles << "    " << average[1]/cycles/L/L/L/L << endl;
    myfile_mag << cycles << "    " << average[3]/cycles/L/L << endl;
    myfile_mag2 << cycles << "    " << average[2]/cycles/L/L/L/L << endl;

  }

  // close the output file
  myfile_eps.close();
  myfile_eps2.close();
  myfile_mag.close();
  myfile_mag2.close();

  return 0;
}

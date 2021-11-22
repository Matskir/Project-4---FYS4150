#include "omp.h"
#include "important_functions.hpp"


//Code used to compute mean energy and magnetisation per spin as well as their squares for temperature points
//The created output files are used in plot_main.py to make plots of the quantities over temperature


//main function
int main(){
  //Initialise energy, magnetisation and arrays
  double E,M;
  double w[17], average[5];

  //Initialise temperature and temperature steps
  double temp;
  double initial_temp = 2.1;
  double final_temp = 2.4;
  double temp_step = 0.005;
  int n = (final_temp-initial_temp)/temp_step;


  //Initialise number of Monte Carlo cycles
  int mcs = 10000;
  double norm = 1/((double) mcs);

  //Create the output files
  std::ofstream myfile_eps;
  std::ofstream myfile_eps2;
  std::ofstream myfile_mag;
  std::ofstream myfile_mag2;

  myfile_eps.open ("outputs_eps_L40_res.txt");
  myfile_eps2.open ("outputs_eps2_L40_res.txt");
  myfile_mag.open ("outputs_mag_L40_res.txt");
  myfile_mag2.open ("outputs_mag2_L40_res.txt");

  //Initialise spin_matrix to be filled later
  int L = 40;
  arma::mat spin_matrix = arma::mat(L,L);

  //For loop that loops over temperature
  #pragma omp ordered
  for (int i=0; i<=n; i++){
    // initialise energy, magnetisation and temperature
    E = M = 0;
    temp = initial_temp + i*temp_step;

    // setup array for possible energy changes
    for( int de =-8; de <= 8; de++) w[de+8] = 0;
    for( int de =-8; de <= 8; de+=4) w[de+8] = exp(-de/temp);

    // initialise array for expectation values
    for( int i = 0; i < 5; i++) average[i] = 0.;

    initialise(L,spin_matrix,E,M);

    for (int cycles = 1; cycles <= mcs; cycles++){
      Metropolis(L, spin_matrix, E, M, w);

      // update expectation values
      average[0] += E; average[1] += E*E;
      average[2] += M; average[3] += M*M; average[4] += fabs(M);
    }
    //Write to the output files
    myfile_eps << temp << "    " << average[0]*norm/L/L << endl;
    myfile_eps2 << temp << "    " << average[1]*norm/(L*L*L*L) << endl;
    myfile_mag << temp << "    " << average[4]*norm/L/L << endl;
    myfile_mag2 << temp << "    " << average[3]*norm/L/L/L/L << endl;
  }
  //Close the output files
  myfile_eps.close();
  myfile_eps2.close();
  myfile_mag.close();
  myfile_mag2.close();
  return 0;
}

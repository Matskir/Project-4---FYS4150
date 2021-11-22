# Project-4---FYS4150

/src contains all source files used in this Project, and are as following:

important_functions.hpp is the main header file and contains important functions that are common for all following .cpp files. 

prob4_5_proj4.cpp is used to generate samples of epsilon, epsilon2, |m| and m^2 used in Problems 4 and 5. The generated txt-files are read by prob4_proj4.py and prob5_proj4.py to create the plots used in the report. The .cpp-file should be run as:

g++ -O3 prob4_5_proj4.cpp -o prob4_5_proj4.exe -larmadillo

./prob4_5_proj4.exe

prob6_proj4.cpp is used to generate epsilon samples to generate normalised histograms to estimate the full probability distribution. The .cpp-file should be run as:

g++ -O3 prob6_proj4.cpp -o prob6_proj4.exe -larmadillo

./prob6_proj4.exe

proj4_main.cpp is the main source file from this study and generate the same samples as prob4_5_proj4.cpp but here as functions of temperature. It creates output files with temperatures in one axis and the other quantity in the second used to solve both Problem 8 and 9. The .cpp-file should be run as:

g++ -O3 proj4_main.cpp -fopenmp -o proj4_main.exe -larmadillo

./proj4_main.exe


/scripts contains all .py files used to compute CV and chi and create all the plots in the report. All python files are here named by the same convention probX_proj4.py for X = 4,5,6,8 and should be run as:

python probX_proj4.py


All .txt-files needed to run the Python scripts are included in /textfiles.

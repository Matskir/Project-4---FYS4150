import numpy as np
import matplotlib.pyplot as plt

#Set font size
import matplotlib
matplotlib.rcParams.update({'font.size': 15})

#Function that reads the files
def read_file(filename):
    infile = open(filename)
    x = []; y = []

    for line in infile:
        elements = line.split()
        x.append(float(elements[0]))
        y.append(float(elements[1]))

    x = np.array(x)
    y = np.array(y)
    infile.close()

    return x,y


#Read input files
cycles_T1, eps_T1 = read_file('output_eps_histo_T1.txt')
cycles_T2, eps_T2 = read_file('output_eps_histo_T2.txt')


#Plot normalised histograms
plt.figure(1)
hist, bin_edges = np.histogram(eps_T1[2000:])
weights_T1 = np.ones_like(eps_T1[2000:])/float(len(eps_T1[2000:]))
plt.hist(x=eps_T1[2000:], bins=10, color='#0504aa',alpha=0.7, rwidth=0.85, weights=weights_T1)
plt.xlabel('$\\epsilon$ [J]')
plt.ylabel('Probability Density [1]')
plt.tight_layout()
plt.savefig('prob_dist_T1.pdf')

plt.figure(2)
hist, bin_edges = np.histogram(eps_T2[2000:])
weights_T2 = np.ones_like(eps_T2[2000:])/float(len(eps_T2[2000:]))
plt.hist(x=eps_T2[2000:], bins=50, color='#0504aa',alpha=0.7, rwidth=0.85, weights=weights_T2)
plt.xlabel('$\\epsilon$ [J]')
plt.ylabel('Probability Density [1]')
plt.tight_layout()
plt.savefig('prob_dist_T2.pdf')
plt.show()

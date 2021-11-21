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


cycles_unordered, eps_unordered = read_file('output_eps_unordered.txt')
cycles_unordered, mag_unordered = read_file('output_mag_unordered.txt')
cycles_ordered, eps_ordered = read_file('output_eps_ordered.txt')
cycles_ordered, mag_ordered = read_file('output_mag_ordered.txt')

cycles_unordered_T2, eps_unordered_T2 = read_file('output_eps_unordered_T2.txt')
cycles_unordered_T2, mag_unordered_T2 = read_file('output_mag_unordered_T2.txt')
cycles_ordered_T2, eps_ordered_T2 = read_file('output_eps_ordered_T2.txt')
cycles_ordered_T2, mag_ordered_T2 = read_file('output_mag_ordered_T2.txt')

plt.figure(1)
plt.plot(cycles_unordered,eps_unordered,label='Unordered')
plt.plot(cycles_ordered,eps_ordered,label='Ordered')
plt.hlines(-1.99598206,cycles_unordered[0],cycles_unordered[-1],color='k',linestyles='--',label='Expected value $\\langle \\epsilon \\rangle = -1.99598206\,\,\,J$')
plt.legend()
plt.ylabel('$\\langle \\epsilon \\rangle /J$')
plt.xlabel('Monte Carlo Cycles')
plt.tight_layout()
plt.savefig('epsilon_unordered.pdf')

plt.figure(2)
plt.plot(cycles_unordered,mag_unordered,label='Unordered')
plt.plot(cycles_ordered,mag_ordered,label='Ordered')
plt.hlines(0.99866074,cycles_unordered[0],cycles_unordered[-1],color='k',linestyles='--',label='Expected value $\\langle |m| \\rangle = 0.99866074$')
plt.legend()
plt.ylabel('$\\langle |m| \\rangle /J$')
plt.xlabel('Monte Carlo Cycles')
plt.tight_layout()
plt.savefig('magnet_unordered.pdf')

plt.figure(3)
plt.plot(cycles_unordered_T2,eps_unordered_T2,label='Unordered')
plt.plot(cycles_ordered_T2,eps_ordered_T2,label='Ordered')
plt.legend()
plt.ylabel('$\\langle \\epsilon \\rangle /J$')
plt.xlabel('Monte Carlo Cycles')
plt.tight_layout()
plt.savefig('epsilon_unordered_T2.pdf')

plt.figure(4)
plt.plot(cycles_unordered_T2,mag_unordered_T2,label='Unordered')
plt.plot(cycles_ordered_T2,mag_ordered_T2,label='Ordered')
plt.legend()
plt.ylabel('$\\langle |m| \\rangle /J$')
plt.xlabel('Monte Carlo Cycles')
plt.tight_layout()
plt.savefig('magnet_unordered_T2.pdf')
plt.show()

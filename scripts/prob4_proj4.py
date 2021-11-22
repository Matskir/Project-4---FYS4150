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


cycles, eps = read_file('output_eps.txt')
cycles, eps2 = read_file('output_eps2.txt')
cycles, mag = read_file('output_mag.txt')
cycles, mag2 = read_file('output_mag2.txt')

fig, ax = plt.subplots()
ax.plot(cycles,eps)
ax.hlines(-1.99598206,cycles[0],cycles[-1],color='k',linestyles='--',label='Expected value $\\langle \\epsilon \\rangle = -1.99598206\,\,\,J$')
ax.set_ylabel('$\\langle \\epsilon \\rangle /J$')
ax.set_xlabel('Monte Carlo Cycles')
ax.legend()
fig.tight_layout()
fig.savefig('epsilon_2x2.pdf')


fig2, ax2 = plt.subplots()
ax2.plot(cycles,mag)
ax2.hlines(0.99866074,cycles[0],cycles[-1],color='k',linestyles='--',label='Expected value $\\langle |m| \\rangle = 0.99866074$')
ax2.set_ylabel('$\\langle |m| \\rangle /J$')
ax2.set_xlabel('Monte Carlo Cycles')
ax2.legend()
fig2.tight_layout()
fig2.savefig('magnet_2x2.pdf')


fig3, ax3 = plt.subplots()
ax3.plot(cycles,4/1*(eps2 - eps**2))
ax3.hlines(0.032082,cycles[0],cycles[-1],color='k',linestyles='--',label='Expected value $C_V/k_B = 0.032082$')
ax3.set_ylabel('$C_V/k_B$')
ax3.set_xlabel('Monte Carlo Cycles')
ax3.legend()
fig3.tight_layout()
fig3.savefig('CV.pdf')

fig4, ax4 = plt.subplots()
ax4.plot(cycles,4/1*(mag2 - mag**2))
ax4.hlines(4.0107115e-3,cycles[0],cycles[-1],color='k',linestyles='--',label='Expected value $\\chi = 4.0107115 \cdot 10^{-3}$')
ax4.set_ylabel('$\\chi$')
ax4.set_xlabel('Monte Carlo Cycles')
ax4.legend()
fig4.tight_layout()
fig4.savefig('susceptibility_2x2.pdf')

plt.show()

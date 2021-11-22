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
temp_40, eps_40 = read_file('outputs_eps_L40_res.txt')
temp_40, eps2_40 = read_file('outputs_eps2_L40_res.txt')
temp_40, mag_40 = read_file('outputs_mag_L40_res.txt')
temp_40, mag2_40 = read_file('outputs_mag2_L40_res.txt')

temp_60, eps_60 = read_file('outputs_eps_L60_res.txt')
temp_60, eps2_60 = read_file('outputs_eps2_L60_res.txt')
temp_60, mag_60 = read_file('outputs_mag_L60_res.txt')
temp_60, mag2_60 = read_file('outputs_mag2_L60_res.txt')

temp_80, eps_80 = read_file('outputs_eps_L80_res.txt')
temp_80, eps2_80 = read_file('outputs_eps2_L80_res.txt')
temp_80, mag_80 = read_file('outputs_mag_L80_res.txt')
temp_80, mag2_80 = read_file('outputs_mag2_L80_res.txt')

temp_100, eps_100 = read_file('outputs_eps_L100_res.txt')
temp_100, eps2_100 = read_file('outputs_eps2_L100_res.txt')
temp_100, mag_100 = read_file('outputs_mag_L100_res.txt')
temp_100, mag2_100 = read_file('outputs_mag2_L100_res.txt')


#Plot
plt.figure(0)
plt.plot(temp_40,eps_40,label='L = 40')
plt.plot(temp_60,eps_60,label='L = 60')
plt.plot(temp_80,eps_80,label='L = 80')
plt.plot(temp_100,eps_100,label='L = 100')
plt.xlabel('Temperature [$J/k_B$]')
plt.ylabel('$\\langle \\epsilon \\rangle$  [J]')
plt.legend()
plt.tight_layout()
plt.savefig('eps_prob8.pdf')

plt.figure(1)
plt.plot(temp_40,mag_40,label='L = 40')
plt.plot(temp_60,mag_60,label='L = 60')
plt.plot(temp_80,mag_80,label='L = 80')
plt.plot(temp_100,mag_100,label='L = 100')
plt.xlabel('Temperature [$J/k_B$]')
plt.ylabel('$\\langle |m| \\rangle$  [1]')
plt.legend()
plt.tight_layout()
plt.savefig('mag_prob8.pdf')

plt.figure(2)
CV_40 = 40**2/(temp_40**2)*(eps2_40-eps_40**2)
CV_60 = 60**2/(temp_60**2)*(eps2_60-eps_60**2)
CV_80 = 80**2/(temp_80**2)*(eps2_80-eps_80**2)
CV_100 = 100**2/(temp_100[4:]**2)*(eps2_100[4:]-eps_100[4:]**2)
plt.plot(temp_40,CV_40,label='L = 40')
plt.plot(temp_60,CV_60,label='L = 60')
plt.plot(temp_80,CV_80,label='L = 80')
plt.plot(temp_100[4:],CV_100,label='L = 100')
plt.ylabel('$C_V$  [$Jk_B$]')
plt.xlabel('Temperature [$J/k_B$]')
plt.legend()
plt.tight_layout()
plt.savefig('CV_prob8.pdf')

plt.figure(3)
X_40 = 40**2/(temp_40)*(mag2_40-mag_40**2)
X_60 = 60**2/(temp_60)*(mag2_60-mag_60**2)
X_80 = 80**2/(temp_80)*(mag2_80-mag_80**2)
X_100 = 100**2/(temp_100[4:])*(mag2_100[4:]-mag_100[4:]**2)

plt.plot(temp_40,X_40,label='L = 40')
plt.plot(temp_60,X_60,label='L = 60')
plt.plot(temp_80,X_80,label='L = 80')
plt.plot(temp_100[4:],X_100,label='L = 100')
plt.ylabel('$\chi$  [1]')
plt.xlabel('Temperature [$J/k_B$]')
plt.legend()
plt.tight_layout()
plt.savefig('chi_prob8.pdf')


"""
Problem 9:
"""
L = np.array([40,60,80,100])
Tc = np.array([temp_40[np.argmax(CV_40)],temp_60[np.argmax(CV_60)],temp_80[np.argmax(CV_80)],temp_100[4:][np.argmax(CV_100)]])
print(Tc)
line = np.polyfit(L,1/Tc,1)
print(line)

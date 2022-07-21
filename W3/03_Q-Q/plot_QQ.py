import numpy as np
import matplotlib.pyplot as plt


# Figure Setting
# Edit the font, font size, and axes width
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 2
fig,ax = plt.subplots()

# constants
eps = 0.00552634935  # vacuum permitivity in e/(V*Angstrom)

Q1 = -2.669 # atomic unit 
Q2 = -2.669 # atomic unit
R = np.linspace(2.8,8.0,100)
## for molecule A and B with their axis align with z-axis
Q_conv = 0.529177**2.0 # conversion unit for Q (from atomic unit to e*A**2.0)
V = Q1*Q2*Q_conv**2.0/(4.0*np.pi*eps*R**5.0)*6.0 

# plot V arising from Q-Q wrt R
ax.plot(R,V,label='q-q')

# read Eb-D of from xTB with E-D.txt
f = open('E-D.txt','r')
lines = f.readlines()
E = []
D = []
diff = []
for l in lines:
    D.append(float(l.split()[0]))
    E.append(float(l.split()[1]))
    V_D = Q1*Q2*Q_conv**2.0/(4.0*np.pi*eps*float(l.split()[0])**5.0)*6.0
    diff.append( float(l.split()[1]) - V_D )


# plot E-D from the previous xTB computations
ax.plot(D,E,label='xTB')

# plot the difference
ax.plot(D,diff,label='xTB - q-q')


ax.plot([0,8.0],[0,0],ls=':',c='black')

# set label for X and Y axis
ax.set_xlabel('Z (Å)',fontsize=18)
ax.set_ylabel(r'E$_b$ (eV)',fontsize=18)

# set x range
ax.set_xlim(2.0,8.0)
ax.legend(loc='best')

fig.tight_layout()
plt.show()


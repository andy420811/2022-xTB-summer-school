import numpy as np
import matplotlib.pyplot as plt


# Figure Setting
# Edit the font, font size, and axes width
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 2
fig,ax = plt.subplots()


# Read energy from monomer
name = 'monomer/xtb.out'
f = open(name,'r')
lines = f.readlines()
for l in lines:
    if 'TOTAL ENERGY' in l:
       tmp = l.split()
       Em = float(tmp[3])

# Read energy from dimer
D  = []
Eb = []
folder = [ 70, 71, 72, 73, 74, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 130, 140, 150, 160, 170, 180, 190, 200]

# Write the Eb and D value into E-D.txt file
fout = open('E-D.txt','w')

for a in folder:
    # Read xtb.out in 'a' folder
    name = str(a)+'/xtb.out'
    f = open(name,'r')
    lines = f.readlines()
    for l in lines:
        if 'TOTAL ENERGY' in l:
           tmp = l.split()
           Ed = float(tmp[3])
           D.append(float(a)*4.0/100.0)
           Eb.append( (Ed - 2.0*Em)*27.2114 )
           fout.write(str(float(a)*4.0/100.0)+'  '+str((Ed - 2.0*Em)*27.2114) +'\n')

print(np.min(Eb))
ax.plot([0,np.max(folder)*4.0/100.0],[0,0],ls=':',c='black')
ax.scatter(D,Eb)

# set label for X and Y axis
ax.set_xlabel('Z (Å)',fontsize=18)
ax.set_ylabel(r'E$_b$ (eV)',fontsize=18)

# set x range
ax.set_xlim(2.0,np.max(folder)*4.0/100.0)

fig.tight_layout()
plt.show()


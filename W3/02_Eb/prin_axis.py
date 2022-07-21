import numpy as np
import sys
from ase.io import read, write
from ase.build import rotate
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# A function to draw the atoms as spheres
def drawSphere(xCenter, yCenter, zCenter, r):
    #draw sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    #shift and scale sphere
    x = r*x + xCenter
    y = r*y + yCenter
    z = r*z + zCenter
    return (x,y,z)

# Read the xyz as ASE Atom object
xyz = read(sys.argv[1])

# Calculate the moment of inertia matrix using ASE 
I = xyz.get_moments_of_inertia(vectors=True)
# I[0] is the eigen values
# I[1] is the eigen vectors
print("I1: ", I[0][0], "v1: ",I[1][0])
print("I2: ", I[0][1], "v2: ",I[1][1])
print("I3: ", I[0][2], "v3: ",I[1][2])


# Calculate the center of mass
COM = xyz.get_center_of_mass()

# Eigen vectors with I in an ascending manner I1<I2<I3
v1,v2,v3 = I[1][0],I[1][1],I[1][2]

# Figure Setting
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.set_xlim(-6,6)
ax.set_ylim(-6,6)
ax.set_zlim(-6,6)

# Color and radius of "C" and "H"
color = {'C':'black','H':'white'}
radius = {'C':0.5,'H':0.25}

# Read xyz coordinate from sys.argv[1]
#12
# energy: -15.879640657013 gnorm: 0.000043854342 xtb: 6.2.2 (655bc02)
#C          -0.74584842394369    1.16750591221085    0.01734592073486

f = open(sys.argv[1],'r')
lines = f.readlines()
for n, l in enumerate(lines):
    if n > 1:
        tmp = l.split()
        x,y,z = float(tmp[1]),float(tmp[2]),float(tmp[3])
        E = tmp[0]
        (xs,ys,zs) = drawSphere(x,y,z,radius[E])
        ax.plot_surface(xs,ys,zs,color=color[E])

# Plot the three principal axis
norm = 6.0
#plot v1
ax.plot([COM[0]-norm*v1[0],COM[0]+norm*v1[0]],[COM[1]-norm*v1[1],COM[1]+norm*v1[1]],[COM[2]-norm*v1[2],COM[2]+norm*v1[2]])
#plot v2
ax.plot([COM[0]-norm*v2[0],COM[0]+norm*v2[0]],[COM[1]-norm*v2[1],COM[1]+norm*v2[1]],[COM[2]-norm*v2[2],COM[2]+norm*v2[2]])
#plot v3
ax.plot([COM[0]-norm*v3[0],COM[0]+norm*v3[0]],[COM[1]-norm*v3[1],COM[1]+norm*v3[1]],[COM[2]-norm*v3[2],COM[2]+norm*v3[2]])

plt.show()


import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

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


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax.view_init(0,90)
color = {'C':'black','H':'white'}
radius = {'C':0.5,'H':0.25}
# Read xyz from xtb_esp.cosmo
# X1      -0.74584842405873      1.16750591233998      0.01734592072579 COSM 1 c  C  0.000
f = open('xtb_esp.cosmo','r')
lines = f.readlines()
for l in lines:
    if 'X1' in l:
        tmp = l.split()
        x,y,z = float(tmp[1]),float(tmp[2]),float(tmp[3])
        E = tmp[-2]
        #print(x,y,z)
        (xs,ys,zs) = drawSphere(x,y,z,radius[E])
        ax.plot_surface(xs,ys,zs,color=color[E])

# Read grid esp from xtb_esp.dat
f = open('xtb_esp.dat','r')
lines = f.readlines()
xs = []
ys = []
zs = []
cs = []
for l in lines:
    tmp = l.split()
    xs.append( float(tmp[0]) )
    ys.append( float(tmp[1]) )
    zs.append( float(tmp[2]) )
    cs.append( float(tmp[3]) )
xs = np.array(xs)*0.529
ys = np.array(ys)*0.529
zs = np.array(zs)*0.529
cs = np.array(cs)

s = ax.scatter(xs,ys,zs,c=cs, cmap='RdBu',alpha=0.9,s=3)

plt.colorbar(s)

ax.set_xlim(-6,6)
ax.set_ylim(-6,6)
ax.set_zlim(-6,6)

plt.show()


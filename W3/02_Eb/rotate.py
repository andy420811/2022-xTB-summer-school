import numpy as np
from ase.io import read, write
from ase.build import rotate
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Read the xyz as Atom object in ASE
xyz = read('xtbopt.xyz')

# Get the moment of inertia of the compound
I = xyz.get_moments_of_inertia(vectors=True)

# Get the center of mass before translation
COM = xyz.get_center_of_mass()
print('Original center of mass: ',COM)

# Get the center of mass after translation COM to (0,0,0)
xyz.translate(-COM)
COM = xyz.get_center_of_mass()
print('Center of mass after translation: ', COM)

# Align the shortest molecular axis to z-axis
xyz.rotate(I[1][2],'z','COM', rotate_cell=False)

# Write out the final structure as new.xyz
xyz.write('aligned_z.xyz')






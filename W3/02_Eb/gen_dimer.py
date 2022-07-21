import sys
import numpy as np
from ase.io import read, write
from ase.build import rotate
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Read the xyz as Atom object in ASE
xyz = read('aligned_z.xyz')
xyz_original = xyz.copy()

# Shift the molecules in z direction with P% of 4.0 Angstrom
v = np.array([0,0,4.0])*float(sys.argv[1])/100.0
xyz.translate(v)
xyz.extend(xyz_original)

# Write out the final structure 
xyz.write(sys.argv[2])


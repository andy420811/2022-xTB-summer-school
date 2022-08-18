import numpy as np
from ase.io import read, write
from ase.thermochemistry import IdealGasThermo

# Read the xyz as Atom object in ASE
#atoms = read('xtbopt.xyz')
atoms = read('b3lyp_H2.xyz')

conv_cm2eV = 1.23981E-4
vib_list = [3739.15] # in cm-1
#vib_list = [4461.2550]
vib_energies = np.array(vib_list)*conv_cm2eV

potentialenergy = -26.7402479136 #in eV 

thermo = IdealGasThermo(vib_energies=vib_energies,
                        potentialenergy=potentialenergy,
                        atoms=atoms,
                        geometry='linear',
                        symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.)


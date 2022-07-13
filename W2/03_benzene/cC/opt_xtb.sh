export OMP_STACKSIZE=4G
ulimit -s unlimited
export OMP_NUM_THREADS=8,1
export MKL_NUM_THREADS=8

xtb -c 1 -u 1 input.xyz --opt normal   > xtb.out

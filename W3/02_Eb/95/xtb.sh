export OMP_STACKSIZE=1G
ulimit -s unlimited
export OMP_NUM_THREADS=1,1
export MKL_NUM_THREADS=1

xtb -c 0 -u 0 input.xyz  > xtb.out

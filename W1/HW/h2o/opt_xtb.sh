export OMP_STACKSIZE=4G
ulimit -s unlimited
export OMP_NUM_THREADS=8,1
export MKL_NUM_THREADS=8

xtb -c 0 -u 0 h2o.xyz --opt normal  > xtb.out

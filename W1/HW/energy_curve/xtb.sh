export OMP_STACKSIZE=8G
ulimit -s unlimited
export OMP_NUM_THREADS=16,1
export MKL_NUM_THREADS=8

for d in $(seq 20 10 500);do
    mkdir $d
    D=$(python3 -c "print(0.74*$d/100)")
    cd $d
    echo -e "2\n\nH 0 0 0\nH $D 0 0" > h2_$d.xyz
    xtb -c 0 -u 0 h2_$d.xyz  > xtb.out
    cd ..
done

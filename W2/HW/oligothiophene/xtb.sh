for i in *;do
    cd $i
    xtb -c 0 -u 0 --opt --molden $i.xyz > xtb.out
    cd ..
done

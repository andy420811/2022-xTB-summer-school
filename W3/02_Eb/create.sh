## for loop
for a in 70 71 72 73 74 75 80 85 90 95 100 105 110 115 120 130 140 150 160 170 180 190 200
do

    ## for each variable a ($a), create a folder
    mkdir $a

    ## copy the xtb running script to folder $a
    cp xtb.sh $a

    ## generate a dimer input xyz file in the folder. the distance is $a% of 4.0 Angstrom
    python gen_dimer.py $a ${a}/input.xyz

    ## enter the folder and run the script
    cd $a
    echo "Running $a now..."
    nohup bash xtb.sh &

    ## leave the $a folder and do the next loop
    cd ..

done

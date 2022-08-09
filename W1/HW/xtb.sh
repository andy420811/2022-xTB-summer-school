export OMP_STACKSIZE=8G
ulimit -s unlimited
export OMP_NUM_THREADS=16,1
export MKL_NUM_THREADS=8

# loop every directory

for d in ./*/ ; do
    cd $d
    files=*.xyz
    for file in $files; do
        filename=$(basename -- "$file")
        extension="${filename##*.}"
        filename="${filename%.*}"
        mkdir "$filename"
        cp $file $filename
        cd "$filename"
        xtb -c 0 -u 0 "$filename".xyz --opt normal  > xtb.out
        cd ..
    done
    cd ..
done

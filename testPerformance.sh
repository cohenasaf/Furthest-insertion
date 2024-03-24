declare -a TSP
TSP=(d198 lin318 fl417 pcb442 u574 p654 rat783 pr1002 u1060 pcb1173 d1291 rl1323 fl1400 u1432 fl1577 d1655 vm1748 rl1889 u2152 pr2392 pcb3038 fl3795)


for element in "${TSP[@]}"
do
    for i in `seq 1 100`
    do
        kernprof -l -v testRandom.py $element
    done
done

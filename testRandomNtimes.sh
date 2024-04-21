declare -a TSP
#TSP=(d198 lin318 fl417 pcb442 u574 p654 rat783 pr1002 u1060 pcb1173 d1291 rl1323 fl1400 u1432 fl1577 d1655 vm1748 rl1889 u2152 pr2392 pcb3038 fl3795)
TSP=(rl11849 usa13509 brd14051 d15112 d18512)
#TSP=(u1060)

for element in "${TSP[@]}"
do
    python3 testRandomNtimes.py $element 50
done

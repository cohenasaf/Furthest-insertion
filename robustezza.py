from TSP import TSP
import sys
import time
import numpy as np

def testEuristicO(name, euristic, m):
    st = time.time()
    euristic(m)
    et = time.time()
    t.calculateCost()
    assert t.verifyTour()
    #print("{:18s} costo: {:.2f}, qualità: {:.4f}, tempo: {:.6f} secondi".format(name, t.cost, t.cost / t.optimalSolution, et - st))
    #return (t.cost / t.optimalSolution, et - st)
    return et - st
    #return t.cost / t.optimalSolution

def testEuristic(name, euristic):
    st = time.time()
    euristic()
    et = time.time()
    t.calculateCost()
    assert t.verifyTour()
    #print("{:18s} costo: {:.2f}, qualità: {:.4f}, tempo: {:.6f} secondi".format(name, t.cost, t.cost / t.optimalSolution, et - st))
    #return (t.cost / t.optimalSolution, et - st)
    return et - st
    #return t.cost / t.optimalSolution


dC = {"eil51": 1, "berlin52": 1, "st70": 2, "pr76": 1, "eil76": 1, "rat99": 1, "kroD100": 3, "kroA100": 1, "kroC100": 1, "kroB100": 1, "kroE100": 1, "rd100": 1, "eil101": 1, "lin105": 1, "pr107": 3, "pr124": 3, "bier127": 2, "ch130": 3, "pr136": 1, "pr144": 3, "kroA150": 3, "ch150": 1, "kroB150": 3, "pr152": 1, "u159": 3, "rat195": 1, "d198": 3, "kroA200": 1, "kroB200": 3, "ts225": 2, "tsp225": 3, "pr226": 1, "gil262": 1, "pr264": 3, "a280": 1, "pr299": 2, "lin318": 3, "linhp318": 3, "rd400": 3, "fl417": 1, "pr439": 2, "pcb442": 3, "d493": 1, "u574": 3, "rat575": 3, "p654": 3, "d657": 3, "u724": 3, "rat783": 3, "pr1002": 2}
dF = {'eil51': 3, 'berlin52': 3, 'st70': 3, 'pr76': 3, 'eil76': 5, 'rat99': 3, 'kroD100': 3, 'kroA100': 3, 'kroC100': 3, 'kroB100': 3, 'kroE100': 3, 'rd100': 3, 'eil101': 5, 'lin105': 3, 'pr107': 3, 'pr124': 3, 'bier127': 6, 'ch130': 3, 'pr136': 3, 'pr144': 3, 'kroA150': 5, 'ch150': 4, 'kroB150': 3, 'pr152': 3, 'u159': 3, 'rat195': 5, 'd198': 6, 'kroA200': 5, 'kroB200': 3, 'ts225': 6, 'tsp225': 4, 'pr226': 3, 'gil262': 6, 'pr264': 6, 'a280': 6, 'pr299': 3, 'lin318': 5, 'linhp318': 5, 'rd400': 6, 'fl417': 3, 'pr439': 6, 'pcb442': 6, 'd493': 6, 'u574': 6, 'rat575': 5, 'p654': 3, 'd657': 6, 'u724': 6, 'rat783': 6, 'pr1002': 6}

TSP_LIB = ['eil51', 'berlin52', 'st70', 'pr76', 'eil76', 'rat99', 'kroD100', 'kroA100', 'kroC100', 'kroB100', 'kroE100', 'rd100', 'eil101', 'lin105', 'pr107', 'pr124', 'bier127', 'ch130', 'pr136', 'pr144', 'kroA150', 'ch150', 'kroB150', 'pr152', 'u159', 'rat195', 'd198', 'kroA200', 'kroB200', 'ts225', 'tsp225', 'pr226', 'gil262', 'pr264', 'a280', 'pr299', 'lin318', 'linhp318', 'rd400', 'fl417', 'pr439', 'pcb442', 'd493', 'u574', 'rat575', 'p654', 'd657', 'u724', 'rat783', 'pr1002', 'u1060', 'vm1084', 'pcb1173', 'd1291', 'rl1304', 'rl1323', 'nrw1379', 'fl1400', 'u1432', 'fl1577', 'd1655', 'vm1748', 'u1817', 'rl1889', 'd2103', 'u2152', 'u2319', 'pr2392', 'pcb3038', 'fl3795', 'fnl4461', 'rl5915', 'rl5934', 'rl11849', 'usa13509', 'brd14051', 'd15112', 'd18512']
name_m = []

NN = []
NI = []
CI = []
FaI = []
FuI = []
for l in TSP_LIB[:30]:
    t = TSP(l, ignoraOpt=True)
    print()
    print("_________________")
    print(t.name)

    a = []
    b = []
    c = []
    d = []
    e = []


    for i in range(100):
        a.append(testEuristic("", t.nearestNeighborRandomStart))
        b.append(testEuristic("", t.nearestInsertionRandomStart))
        c.append(testEuristicO("", t.cheapestInsertionOttimizzatoRandomStart, dC[t.name]))
        d.append(testEuristic("", t.farthestInsertionRandomStart))
        e.append(testEuristic("", t.furthestInsertionRandomStart))

    NN.append(np.var(a))
    NI.append(np.var(b))
    CI.append(np.var(c))
    FaI.append(np.var(d))
    FuI.append(np.var(e))

print(NN)
print(NI)
print(CI)
print(FaI)
print(FuI)
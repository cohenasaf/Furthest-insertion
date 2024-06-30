from TSP import TSP
import sys
import time

def testEuristicO(name, euristic, m):
    st = time.time()
    euristic(m)
    et = time.time()
    t.calculateCost()
    assert t.verifyTour()
    print("m = {} -> {:18s} costo: {:.2f}, qualità: {:.4f}, tempo: {:.6f} secondi".format(m, name, t.cost, t.cost / t.optimalSolution, et - st))
    return (t.cost / t.optimalSolution, et - st)

def testEuristic(name, euristic):
    st = time.time()
    euristic()
    et = time.time()
    t.calculateCost()
    assert t.verifyTour()
    print("{:18s} costo: {:.2f}, qualità: {:.4f}, tempo: {:.6f} secondi".format(name, t.cost, t.cost / t.optimalSolution, et - st))
    return (t.cost / t.optimalSolution, et - st)

TSP_LIB = ['eil51', 'berlin52', 'st70', 'pr76', 'eil76', 'rat99', 'kroD100', 'kroA100', 'kroC100', 'kroB100', 'kroE100', 'rd100', 'eil101', 'lin105', 'pr107', 'pr124', 'bier127', 'ch130', 'pr136', 'pr144', 'kroA150', 'ch150', 'kroB150', 'pr152', 'u159', 'rat195', 'd198', 'kroA200', 'kroB200', 'ts225', 'tsp225', 'pr226', 'gil262', 'pr264', 'a280', 'pr299', 'lin318', 'linhp318', 'rd400', 'fl417', 'pr439', 'pcb442', 'd493', 'u574', 'rat575', 'p654', 'd657', 'u724', 'rat783', 'pr1002', 'u1060', 'vm1084', 'pcb1173', 'd1291', 'rl1304', 'rl1323', 'nrw1379', 'fl1400', 'u1432', 'fl1577', 'd1655', 'vm1748', 'u1817', 'rl1889', 'd2103', 'u2152', 'u2319', 'pr2392', 'pcb3038', 'fl3795', 'fnl4461', 'rl5915', 'rl5934', 'rl11849', 'usa13509', 'brd14051', 'd15112', 'd18512']
dC = dict()
dF = dict()

for l in TSP_LIB[:50]:
    t = TSP(l, ignoraOpt=True)
    print()
    print("_________________")
    print(time.ctime(time.time()))
    print(t.name)

    t.calculateOptimalCost()

    r = []
    last_m = 1
    for m in range(8, 0, -1):
        r.append(testEuristicO("cheapestInsertionOttimizzato", t.cheapestInsertionOttimizzato, m))
        if len(r) >= 2 and r[-1][0] != r[-2][0]:
            last_m = m + 1
            break
    print("Cheapest", t.name, "->", last_m)
    dC[t.name] = last_m

    r = []
    last_m = 1
    for m in range(10, 0, -1):
        r.append(testEuristicO("furthestInsertionOttimizzato", t.furthestInsertionOttimizzato, m))
        if len(r) >= 2 and r[-1][0] != r[-2][0]:
            last_m = m + 1
            break
    print("Furthest", t.name, "->", last_m)
    dF[t.name] = last_m

print(dC)
print(dF)
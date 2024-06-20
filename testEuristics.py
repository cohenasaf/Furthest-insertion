from TSP import TSP
import re
import sys
import time

def testEuristic(name, euristic):
    st = time.time()
    euristic()
    et = time.time()
    t.calculateCost()
    assert t.verifyTour()
    #print(f"{name}, costo: {t.cost}, qualità: {t.cost / t.optimalSolution}, tempo: {et - st} secondi.")
    print("{:18s} costo: {:.2f}, qualità: {:.4f}, tempo: {:.6f} secondi".format(name, t.cost, t.cost / t.optimalSolution, et - st))
    r.append(t.cost)

#TSP_LIB = ['eil51', 'berlin52', 'st70', 'pr76', 'eil76', 'rat99', 'kroD100', 'kroA100', 'kroC100', 'kroB100', 'kroE100', 'rd100', 'eil101', 'lin105', 'pr107', 'pr124', 'bier127', 'ch130', 'pr136', 'pr144', 'kroA150', 'ch150', 'kroB150', 'pr152', 'u159', 'rat195', 'd198', 'kroA200', 'kroB200', 'ts225', 'tsp225', 'pr226', 'gil262', 'pr264', 'a280', 'pr299', 'lin318', 'linhp318', 'rd400', 'fl417', 'pr439', 'pcb442', 'd493', 'u574', 'rat575', 'p654', 'd657', 'u724', 'rat783', 'pr1002', 'u1060', 'vm1084', 'pcb1173', 'd1291', 'rl1304', 'rl1323', 'nrw1379', 'fl1400', 'u1432', 'fl1577', 'd1655', 'vm1748', 'u1817', 'rl1889', 'd2103', 'u2152', 'u2319', 'pr2392', 'pcb3038', 'fl3795', 'fnl4461', 'rl5915', 'rl5934', 'rl11849', 'usa13509', 'brd14051', 'd15112', 'd18512']
l = sys.argv[1]
r = []
t = TSP(l, ignoraOpt=True)
print()
print("_________________")
print(t.name)

t.calculateOptimalCost()

testEuristic("randomInsertion", t.randomInsertion)
testEuristic("nearestNeighbor", t.nearestNeighbor)
testEuristic("nearestInsertion", t.nearestInsertion)
testEuristic("cheapestInsertion", t.cheapestInsertion)
testEuristic("farthestInsertion", t.farthestInsertion)
testEuristic("furthestInsertion", t.furthestInsertion)
#testEuristic("nearestNeighbourRandom", t.nearestInsertionRandomStart)

t.calculateOptimalCost()
print("Optimal", t.optimalSolution)
from TSP import TSP
import re
import sys

def estraiNum(s):
    for i in range(len(s)):
        if s[i:].isdigit():
            return int(s[i:])

TSP_LIB = ['eil51', 'berlin52', 'st70', 'pr76', 'eil76', 'rat99', 'kroD100', 'kroA100', 'kroC100', 'kroB100', 'kroE100', 'rd100', 'eil101', 'lin105', 'pr107', 'pr124', 'bier127', 'ch130', 'pr136', 'pr144', 'kroA150', 'ch150', 'kroB150', 'pr152', 'u159', 'rat195', 'd198', 'kroA200', 'kroB200', 'ts225', 'tsp225', 'pr226', 'gil262', 'pr264', 'a280', 'pr299', 'lin318', 'linhp318', 'rd400', 'fl417', 'pr439', 'pcb442', 'd493', 'u574', 'rat575', 'p654', 'd657', 'u724', 'rat783', 'pr1002', 'u1060', 'vm1084', 'pcb1173', 'd1291', 'rl1304', 'rl1323', 'nrw1379', 'fl1400', 'u1432', 'fl1577', 'd1655', 'vm1748', 'u1817', 'rl1889', 'd2103', 'u2152', 'u2319', 'pr2392', 'pcb3038', 'fl3795', 'fnl4461', 'rl5915', 'rl5934', 'rl11849', 'usa13509', 'brd14051', 'd15112', 'd18512']
TSP_LIB = ["d198", "lin318", "fl417", "pcb442", "u574"]
results = []
l = sys.argv[1]
#if estraiNum(l) > 500:
#    continue
r = []
t = TSP(l, ignoraOpt=True)
print()
print("_________________")
print(t.name)

t.nearestInsertionRandomStart()
t.calculateCost()
assert t.verifyTour()
print("nearestInsertion", t.cost)
r.append(t.cost)

t.cheapestInsertionRandomStart()
t.calculateCost()
assert t.verifyTour()
print("cheapestInsertion", t.cost)
r.append(t.cost)

t.farthestInsertionRandomStart()
t.calculateCost()
assert t.verifyTour()
print("farthestInsertion", t.cost)
r.append(t.cost)

t.furthestInsertionRandomStart()
t.calculateCost()
assert t.verifyTour()
print("furthestInsertion", t.cost)
r.append(t.cost)

t.calculateOptimalCost()
assert t.verifyTour()
print("Optimal", t.optimalSolution)
r.append(t.optimalSolution)
r.append(l)
print(r)

results.append(tuple(r))
results.sort()

print()
print(results)
print(len(results))
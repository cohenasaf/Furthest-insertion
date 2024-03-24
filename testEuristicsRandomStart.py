from TSP import TSP
import re
import sys

def estraiNum(s):
    for i in range(len(s)):
        if s[i:].isdigit():
            return int(s[i:])

TSP_LIB = ["a280", "berlin52", "bier127", "brd14051", "ch130", "ch150", "d198", "d493", "d657", "d1291", "d1655", "d2103", "d15112", "d18512", "eil51", "eil76", "eil101", "fl417", "fl1400", "fl1577", "fl3795", "fnl4461", "gil262", "kroA100", "kroA150", "kroA200", "kroB100", "kroB150", "kroB200", "kroC100", "kroD100", "kroE100", "lin105", "lin318", "linhp318", "nrw1379", "p654", "pcb442", "pcb1173", "pcb3038", "pr76", "pr107", "pr124", "pr136", "pr144", "pr152", "pr226", "pr264", "pr299", "pr439", "pr1002", "pr2392", "rat99", "rat195", "rat575", "rat783", "rd100", "rd400", "rl1304", "rl1323", "rl1889", "rl5915", "rl5934", "rl11849", "st70", "ts225", "tsp225", "u159", "u574", "u724", "a280", "berlin52", "bier127", "brd14051", "ch130", "ch150", "d198", "d493", "d657", "d1291", "d1655", "d2103", "d15112", "d18512", "eil51", "eil76", "eil101", "fl417", "fl1400", "fl1577", "fl3795", "fnl4461", "gil262", "kroA100", "kroA150", "kroA200", "kroB100", "kroB150", "kroB200", "kroC100", "kroD100", "kroE100", "lin105", "lin318", "linhp318", "nrw1379", "p654", "pcb442", "pcb1173", "pcb3038", "pr76", "pr107", "pr124", "pr136", "pr144", "pr152", "pr226", "pr264", "pr299", "pr439", "pr1002", "pr2392", "rat99", "rat195", "rat575", "rat783", "rd100", "rd400", "rl1304", "rl1323", "rl1889", "rl5915", "rl5934", "rl11849", "st70", "ts225", "tsp225", "u159", "u574", "u724", "u1060", "u1432", "u1817", "u2152", "u2319", "usa13509", "vm1084", "vm1748", "u1817", "u2152", "u2319", "usa13509", "vm1084", "vm1748"]
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
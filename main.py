from TSP import TSP

#t = TSP("a280")
t = TSP("berlin52")

t.cheapestInsertion()
t.calculateCost()
assert t.verifyTour()
print("cheapestInsertion", t.cost)

t.randomInsertion()
t.calculateCost()
assert t.verifyTour()
print("randomInsertion", t.cost)

t.nearestInsertion()
t.calculateCost()
assert t.verifyTour()
print("nearestInsertion", t.cost)

t.farthestInsertion()
t.calculateCost()
assert t.verifyTour()
print("farthestInsertion", t.cost)

t.furthestInsertion()
t.calculateCost()
assert t.verifyTour()
print("furthestInsertion", t.cost)

t.nearestInsertion()
t.calculateCost()
assert t.verifyTour()
print("nearestInsertion", t.cost)

t.calculateOptimalCost()
assert t.verifyTour()
print("Optimal", t.cost)

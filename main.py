from TSP import TSP

#t = TSP("a280")
t = TSP("berlin52")

t.cheapestInsertion()
t.calculateCost()
print("cheapestInsertion", t.cost)

t.randomInsertion()
t.calculateCost()
print("randomInsertion", t.cost)

t.nearestInsertion()
t.calculateCost()
print("nearestInsertion", t.cost)

t.farthestInsertion()
t.calculateCost()
print("farthestInsertion", t.cost)

t.furthestInsertion()
t.calculateCost()
print("furthestInsertion", t.cost)

t.nearestInsertion()
t.calculateCost()
print("nearestInsertion", t.cost)

t.calculateOptimalCost()
print("Optimal", t.cost)

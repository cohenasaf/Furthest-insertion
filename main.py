from TSP import TSP

t = TSP("a280")
#t = TSP("berlin52")

t.cheapestInsertion()
t.calculateCost()
print("cheapest", t.cost)

t.randomInsertion()
t.calculateCost()
print("random", t.cost)

t.calculateOptimalCost()
print("opt", t.cost)

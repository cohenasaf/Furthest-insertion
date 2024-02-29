from TSP import TSP

t = TSP("a280")
#t = TSP("berlin52")
t.randomInsertion()
t.calculateCost()
print(t.cost)
t.calculateOptimalCost()
print(t.cost)
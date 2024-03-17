Here is a possible implementation of the cheapest insertion heuristic for 
the Traveling Salesman Problem (TSP) in Python, with a time complexity of O(n^2 * log(n)):
```python
import math

def cheapest_insertion(graph, start):
    # Initialize the tour with the starting city
    tour = [start]

    # Iterate over all cities in the graph
    for i in range(1, len(graph)):
        # Find the nearest neighbor of the current city in the tour
        nearest_neighbor = tour[-1]
        min_distance = math.inf
        for j in range(len(tour)):
            if graph[tour[j]][i] < min_distance:
                min_distance = graph[tour[j]][i]
                nearest_neighbor = tour[j]

        # Insert the new city into the tour at the correct position
        for k in range(len(tour)):
            if tour[k] == nearest_neighbor:
                tour.insert(k+1, i)
                break
    return tour
```
This implementation uses a similar approach to the Nearest Neighbor heuristic, but with an additional optimization step to find the nearest neighbor of the current city in the tour. 
This is done by first finding the minimum distance between the current city and all cities in the tour, and then selecting the nearest neighbor based on this value.

The time complexity of this implementation is O(n^2 * log(n)) because it involves two nested loops, with the outer loop iterating over all cities in the graph and the inner loop 
iterating over all cities in the tour. The inner loop has a constant number of iterations (i.e., the length of the tour), so the time complexity of this step is O(n). The outer loop 
has a linear number of iterations (i.e., the number of cities in the graph), so the time complexity of this step is also O(n). Therefore, the overall time complexity of this 
implementation is O(n^2 * log(n)).

It's worth noting that this implementation assumes that the distance between each pair of cities is stored in the graph data structure. If the distances are instead stored as a 
separate matrix or list, then the time complexity would be slightly different. In general, the time complexity of a TSP solution will depend on the specific representation used for the
graph and the specific optimization techniques employed by the algorithm.
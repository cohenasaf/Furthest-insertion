import heapq

q = []
heapq.heappush(q, (500, 1))
heapq.heappush(q, (300, 1))
heapq.heappush(q, (200, 2))

print(heapq.heappop(q))
print(q)
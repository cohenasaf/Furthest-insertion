import math
import random
import sys

class TSP:
    def __init__(self, name):
        self.openTSP(name)

    def distance(self, a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    def openTSP(self, name):
        # estraggo i dati delle coordinate euclidee
        f = open(f"ALL-TSP/{name}.tsp")
        self.numCity = -1
        i = 0
        data = False
        self.coord = []
        for line in f:
            if "EOF" in line:
                break
            if data:
                line = line.replace("  ", " ").replace("  ", " ").replace("\n", "").strip()
                if "." in line.split(" ")[1]:
                    self.coord.append([int(float(line.split(" ")[1])), int(float(line.split(" ")[2]))])
                else:
                    self.coord.append([int(line.split(" ")[1]), int(line.split(" ")[2])])
            if "DIMENSION" in line:
                self.numCity = int(line.split(": ")[1])
            if "NODE_COORD_SECTION" in line:
                data = True
        f.close()

        self.adj = [[0 for _ in range(self.numCity)] for _ in range(self.numCity)]
        for i in range(self.numCity):
            for j in range(i):
                if i == j:
                    continue
                else:
                    self.adj[i][j] = self.adj[j][i] = self.distance(self.coord[i], self.coord[j])

        # leggo il persorso ottimale
        f = open(f"ALL-TSP/{name}.opt.tour")
        self.optTour = [-1 for _ in range(self.numCity)]
        self.tour = [-1 for _ in range(self.numCity)]
        data = False
        i = 0
        for line in f:
            if "-1" in line:
                break
            if data:
                # considero i nodi del grafo a partire da 0 e non da 1 come su TSP LIB
                self.optTour[i] = int(line) - 1
                i += 1
            if "TOUR_SECTION" in line:
                data = True
        f.close()
        
    def calculateCost(self):
        self.cost = 0
        for i in range(self.numCity - 1):
            self.cost += self.adj[self.tour[i]][self.tour[i + 1]]
        self.cost += self.adj[self.tour[self.numCity - 1]][self.tour[0]]
    
    def calculateOptimalCost(self):
        self.cost = 0
        for i in range(self.numCity - 1):
            self.cost += self.adj[self.optTour[i]][self.optTour[i + 1]]
        self.cost += self.adj[self.optTour[self.numCity - 1]][self.optTour[0]]

    def randomInsertion(self):
        self.tour = [x for x in range(self.numCity)]
        random.shuffle(self.tour)
    
    def nearestInsertion(self):
        self.tour = [-1, -1]
        self.tour[0] = 0
        self.tour[1] = 1
        cost = sys.maxsize
        visited = set()
        #cerco il più vicino a 0
        for i in range(1, self.numCity):
            if self.adj[0][i] < cost:
                cost = self.adj[0][i]
                self.tour[1] = i
        visited.add(self.tour[0])
        visited.add(self.tour[1])
        self.tour = self.tour[:2]

        while len(self.tour) < self.numCity:
            cost = sys.maxsize
            j = r = pos = -1
            for r2 in set(range(self.numCity)).difference(visited):
                for pos2, j2 in enumerate(self.tour):
                    if self.adj[r2][j2] < cost:
                        cost = self.adj[r2][j2]
                        j = j2
                        r = r2
                        pos = pos2
            # cerco di inserirlo nel modo migliore possibile
            if self.adj[self.tour[(pos + 1) % len(self.tour)]][r] + self.adj[r][j] - self.adj[self.tour[(pos + 1) % len(self.tour)]][j] > \
            self.adj[self.tour[(pos - 1) % len(self.tour)]][r] + self.adj[r][j] - self.adj[self.tour[(pos - 1) % len(self.tour)]][j]:
                self.tour.insert(pos + 1, r)
            else:
                self.tour.insert(pos, r)
            visited.add(r)
            
        self.calculateCost()
    
    def cheapestInsertion(self):
        self.tour = [-1, -1]
        self.tour[0] = 0
        self.tour[1] = 1
        cost = sys.maxsize
        visited = set()
        #cerco il più vicino a 0
        for i in range(1, self.numCity):
            if self.adj[0][i] < cost:
                cost = self.adj[0][i]
                self.tour[1] = i
        visited.add(self.tour[0])
        visited.add(self.tour[1])
        self.tour = self.tour[:2]

        while len(self.tour) < self.numCity:
            cost = sys.maxsize
            pos = r = -1
            for p in range(len(self.tour) - 1):
                for r2 in set(range(self.numCity)).difference(visited):
                    if self.adj[self.tour[p]][r2] + self.adj[r2][self.tour[p + 1]] - self.adj[self.tour[p]][self.tour[p + 1]] < cost:
                        cost = self.adj[self.tour[p]][r2] + self.adj[r2][self.tour[p + 1]] - self.adj[self.tour[p]][self.tour[p + 1]]
                        r = r2
                        pos = p
            
            # considero anche il caso di inserimento tra l'ultimo elemento e il primo (ciclo)
            p = len(self.tour) - 1
            for r2 in set(range(self.numCity)).difference(visited):
                if self.adj[self.tour[p]][r2] + self.adj[r2][self.tour[0]] - self.adj[self.tour[p]][self.tour[0]] < cost:
                    cost = self.adj[self.tour[p]][r2] + self.adj[r2][self.tour[0]] - self.adj[self.tour[p]][self.tour[0]]
                    r = r2
                    pos = p
                visited.add(r)
            self.tour.insert(pos + 1, r)

        self.calculateCost()
import math
import random
import sys
import numpy as np

class TSP:
    def __init__(self, name, ignoraOpt=False):
        self.ignoraOpt = ignoraOpt
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

        if not self.ignoraOpt:
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
        else:
            self.optTour = [-1 for _ in range(self.numCity)]
            self.tour = [-1 for _ in range(self.numCity)]
        
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
    
    def verifyTour(self):
        for i in range(self.numCity):
            if not i in self.tour:
                print(f"ERRORE, manca {i}")
                return False
            if self.tour.count(i) != 1:
                print(f"ERRORE, manca il numero {i} risulta esserci {self.tour.count(i)}")
                return False
        return True

    #@profile
    def randomInsertion(self):
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
            r = random.sample(set(range(self.numCity)).difference(visited), 1)[0]
            visited.add(r)
            pos = -1
            cost = sys.maxsize
            for pos2 in range(len(self.tour) - 1):
                if self.adj[self.tour[pos2]][r] + self.adj[self.tour[pos2 + 1]][r] - self.adj[self.tour[pos2]][self.tour[pos2 + 1]] < cost:
                    cost = self.adj[self.tour[pos2]][r] + self.adj[self.tour[pos2 + 1]][r] - self.adj[self.tour[pos2]][self.tour[pos2 + 1]]
                    pos = pos2
            self.tour.insert(pos + 1, r)
        self.calculateCost()
        
    #@profile
    def nearestNeighbor(self):
        self.tour = [0]
        visited = set()
        visited.add(0)
        while len(self.tour) < self.numCity:
            cost = sys.maxsize
            j = -1
            for j2 in set(range(self.numCity)).difference(visited):
                if self.adj[self.tour[-1]][j2] < cost:
                    cost = self.adj[self.tour[-1]][j2]
                    j = j2
            self.tour.append(j)
        self.calculateCost()
    
    @profile
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
    
    @profile
    def nearestInsertionNEW(self):
        n = self.numCity
        distances = np.array(self.adj)
        path = [0]  # Inizia da una città arbitraria, in questo caso la prima
        in_path = {0}
        min_distance_to_path = np.inf * np.ones(n)
        nearest_city_to_path = np.zeros(n, dtype=int)

        # Inizializza le distanze minime e le città più vicine per ogni città non nel percorso
        for i in range(1, n):
            min_distance_to_path[i] = distances[0, i]
            nearest_city_to_path[i] = 0

        while len(path) < n:
            # Trova la città non inserita più vicina a qualsiasi città nel percorso
            to_insert = np.argmin(min_distance_to_path)
            min_distance_to_path[to_insert] = np.inf

            # Trova la posizione ottimale per inserire la città trovata
            best_increase = np.inf
            best_position = None
            for i in range(len(path)):
                next_i = (i + 1) % len(path)
                increase = distances[path[i], to_insert] + distances[to_insert, path[next_i]] - distances[path[i], path[next_i]]
                if increase < best_increase:
                    best_increase = increase
                    best_position = i + 1

            path.insert(best_position, to_insert)
            in_path.add(to_insert)

            # Aggiorna le distanze minime e le città più vicine per ogni città non nel percorso
            for i in range(n):
                if i not in in_path and distances[to_insert, i] < min_distance_to_path[i]:
                    min_distance_to_path[i] = distances[to_insert, i]
                    nearest_city_to_path[i] = to_insert

        self.tour = path
        self.calculateCost()
    
    #@profile
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

    #@profile
    def farthestInsertion(self):
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
            cost = -1
            j = r = pos = -1
            for r2 in set(range(self.numCity)).difference(visited):
                for pos2, j2 in enumerate(self.tour):
                    if self.adj[r2][j2] > cost:
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

    #@profile
    def furthestInsertion(self):
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
            cost = -1
            pos = r = -1
            for p in range(len(self.tour) - 1):
                for r2 in set(range(self.numCity)).difference(visited):
                    if self.adj[self.tour[p]][r2] + self.adj[r2][self.tour[p + 1]] - self.adj[self.tour[p]][self.tour[p + 1]] > cost:
                        cost = self.adj[self.tour[p]][r2] + self.adj[r2][self.tour[p + 1]] - self.adj[self.tour[p]][self.tour[p + 1]]
                        r = r2
                        pos = p
            
            # considero anche il caso di inserimento tra l'ultimo elemento e il primo (ciclo)
            p = len(self.tour) - 1
            for r2 in set(range(self.numCity)).difference(visited):
                if self.adj[self.tour[p]][r2] + self.adj[r2][self.tour[0]] - self.adj[self.tour[p]][self.tour[0]] > cost:
                    cost = self.adj[self.tour[p]][r2] + self.adj[r2][self.tour[0]] - self.adj[self.tour[p]][self.tour[0]]
                    r = r2
                    pos = p
            visited.add(r)
            self.tour.insert(pos + 1, r)

        self.calculateCost()
import math
import random
import sys
import numpy as np
import heapq

class TSP:
    def __init__(self, name, ignoraOpt=False):
        self.ignoraOpt = ignoraOpt
        self.openTSP(name)
        self.name = name
        self.optimalSolution = soluzioneOttima[name]

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
            if line == "":
                continue
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
    
    def openRandomTSP(self, n):
        self.name = "random"
        self.numCity = n
        self.adj = [[0 for _ in range(self.numCity)] for _ in range(self.numCity)]
        for i in range(self.numCity):
            for j in range(i):
                if i == j:
                    continue
                else:
                    self.adj[i][j] = self.adj[j][i] = random.randint(0, 1000)
        
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
                print(f"ERRORE, il numero {i} risulta esserci {self.tour.count(i)} volte")
                return False
        return True

    # sceglie casualmente il nodo da inserire e lo inserisce casualmente
    def randomInsertion2(self):
        tour = []
        notInTour = [x for x in range(self.numCity)]
        random.shuffle(notInTour)
        for i in notInTour:
            tour.insert(random.randint(0, len(tour)), i)
        self.tour = tour
        self.calculateCost()

    def randomInsertion(self):
        # sceglie casualmente il nodo da inserisce MA lo inserisce nel modo migilore possibile (minimizzando l'inserimento)
        n = self.numCity
        distances = np.array(self.adj)
        path = [0]  # Inizia da una città arbitraria, in questo caso la prima
        in_path = {0}
        notInPath = [x for x in range(1, n)]
        random.shuffle(notInPath)

        while len(path) < n:
            # Trova la città non inserita più vicina a qualsiasi città nel percorso
            to_insert = notInPath.pop()
            # Trova la posizione ottimale per inserire la città trovata
            best_increase = np.inf
            best_position = None
            for i in range(len(path)):
                next_i = (i + 1) % len(path)
                increase = distances[path[i], to_insert] + distances[to_insert, path[next_i]] - distances[path[i], path[next_i]]
                if increase < best_increase:
                    best_increase = increase
                    best_position = next_i

            path.insert(best_position, to_insert)
            in_path.add(to_insert)

        self.tour = path
        self.calculateCost()
        
    def nearestNeighbor(self):
        self.tour = [0]
        visited = set([0])
        notVisited = set(range(1, self.numCity))
        while len(self.tour) < self.numCity:
            cost = np.inf
            j = -1
            for j2 in notVisited:
                if self.adj[self.tour[-1]][j2] < cost:
                    cost = self.adj[self.tour[-1]][j2]
                    j = j2
            self.tour.append(j)
            visited.add(j)
            notVisited.remove(j)
        self.calculateCost()
    
    def nearestInsertion(self):
        # inizializzo il path con i due nodi più vicini
        n = self.numCity
        distances = np.array(self.adj)
        path = [0, 0]

        minDist = np.inf
        for i in range(n):
            for j in range(0, i):
                if distances[i][j] < minDist:
                    path[0], path[1] = i, j
                    minDist = distances[i][j]
        in_path = {path[0], path[1]}


        # Inizializza le distanze minime e le città più vicine per ogni città non nel percorso
        h = []
        for i in set(range(n)) - in_path:
            h.append((min(distances[path[0], i], distances[path[1], i]), i))
        heapq.heapify(h)

        while len(path) < n:
            # Trova la città non inserita più vicina a qualsiasi città nel percorso
            _, to_insert = heapq.heappop(h)

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
            for i, (cost, node) in enumerate(h):
                if node not in in_path and distances[to_insert, node] < cost:
                    h[i] = (distances[to_insert, node], node)
            heapq.heapify(h)

        self.tour = path
        self.calculateCost()
    
    def cheapestInsertion(self):
        n = self.numCity
        adj = np.array(self.adj)
        distances = np.array(self.adj)
        path = [0, 0]

        minDist = np.inf
        for i in range(n):
            for j in range(0, i):
                if distances[i][j] < minDist:
                    path[0], path[1] = i, j
                    minDist = distances[i][j]
        in_path = {path[0], path[1]}

        h = []
        for i in set(range(n)) - in_path:
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h.append((cost, i, path[0], path[1]))
        heapq.heapify(h)

        while len(path) < n:
            # Trova la città non inserita più vicina a qualsiasi città nel percorso
            (_, to_ins, _, _) = heapq.heappop(h)

            # Trova la posizione ottimale per inserire la città trovata
            best_increase = np.inf
            best_pos = None
            for i in range(len(path)):
                next_i = (i + 1) % len(path)
                increase = adj[path[i], to_ins] + adj[to_ins, path[next_i]] - adj[path[i], path[next_i]]
                if increase < best_increase:
                    best_increase = increase
                    best_pos = next_i
            in_path.add(to_ins)

            # A - B - C

            # Aggiorna le distanze minime e le città più vicine per ogni città non nel percorso
            for i, (cost, node, nodeLeft, nodeRight) in enumerate(h):
                # se ho inserito to_ins proprio tra nodeLeft e nodeRight: ricalcolo completamente il costo migliore
                if node not in in_path and nodeLeft == path[(best_pos - 1) % len(path)] and nodeRight == path[(best_pos + 1) % len(path)]:
                    best_cost = np.inf
                    posL, posR = -1, -1
                    for i2 in range(len(path)):
                        next_i = (i2 + 1) % len(path)
                        insertion_cost = adj[path[i2]][node] + adj[node][path[next_i]] - adj[path[i2]][path[next_i]]
                        if best_cost > insertion_cost:
                            best_cost, posL, posR = insertion_cost, i2, next_i
                    h[i] = (best_cost, node, posL, posR)
                # se il nuovo arco a sinistra permette un inserimento migliore di cost, quindi:
                # path[best_pos - 1] -- node -- to_ins
                if node not in in_path and adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins] < cost:
                    new_cost = adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins]
                    h[i] = (new_cost, node, path[(best_pos - 1) % len(path)], to_ins)
                # se il nuovo arco a destra permette un inserimento migliore di cost, quindi:
                # to_ins -- node -- path[best_pos + 1] 
                    best_pos = (best_pos + 1) % (len(path))
                if node not in in_path and adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]] < cost:
                    new_cost = adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]]
                    h[i] = (new_cost, node, to_ins, path[(best_pos + 1) % (len(path))])
            heapq.heapify(h)

        self.tour = path
        self.calculateCost()

    def farthestInsertion(self):
        n = self.numCity
        distances = np.array(self.adj)
        path = [0, 0]

        maxDist = 0
        for i in range(n):
            for j in range(0, i):
                if distances[i][j] > maxDist:
                    path[0], path[1] = i, j
                    maxDist = distances[i][j]
        in_path = {path[0], path[1]}


        # Inizializza le distanze minime e le città più vicine per ogni città non nel percorso
        h = []
        for i in set(range(n)) - in_path:
            h.append((min(distances[path[0], i], distances[path[1], i]), i))
        heapq.heapify(h)

        while len(path) < n:
            # Trova la città non inserita più vicina a qualsiasi città nel percorso
            _, to_insert = heapq.heappop(h)

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
            for i, (cost, node) in enumerate(h):
                cost *= -1
                # cerco comunque di minimizzare distances!
                if node not in in_path and distances[to_insert, node] < cost:
                    h[i] = (-distances[to_insert, node], node)
            heapq.heapify(h)

        self.tour = path
        self.calculateCost()

    def furthestInsertion(self):
        n = self.numCity
        adj = np.array(self.adj)
        distances = np.array(self.adj)
        path = [0, 0]

        maxDist = 0
        for i in range(n):
            for j in range(0, i):
                if distances[i][j] > maxDist:
                    path[0], path[1] = i, j
                    maxDist = distances[i][j]
        in_path = {path[0], path[1]}

        h = []
        for i in set(range(n)) - in_path:
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h.append((-cost, i, path[0], path[1]))
        heapq.heapify(h)

        while len(path) < n:
            # Trova la città non inserita più lontana a qualsiasi città nel percorso
            (_, to_ins, _, _) = heapq.heappop(h)

            # Trova la posizione ottimale per inserire la città trovata
            best_increase = np.inf
            best_pos = None
            for i in range(len(path)):
                next_i = (i + 1) % len(path)
                increase = adj[path[i], to_ins] + adj[to_ins, path[next_i]] - adj[path[i], path[next_i]]
                if increase < best_increase:
                    best_increase = increase
                    best_pos = next_i

            path.insert(best_pos, to_ins)
            in_path.add(to_ins)

            # Aggiorna le distanze minime e le città più vicine per ogni città non nel percorso
            for i, (cost, node, nodeLeft, nodeRight) in enumerate(h):
                cost *= -1
                # se ho inserito to_ins proprio tra nodeLeft e nodeRight: ricalcolo completamente il costo migliore
                if node not in in_path and nodeLeft == path[(best_pos - 1) % len(path)] and nodeRight == path[(best_pos + 1) % len(path)]:
                    best_cost = np.inf
                    posL, posR = -1, -1
                    for i2 in range(len(path)):
                        next_i = (i2 + 1) % len(path)
                        insertion_cost = adj[path[i2]][node] + adj[node][path[next_i]] - adj[path[i2]][path[next_i]]
                        if best_cost > insertion_cost:
                            best_cost, posL, posR = insertion_cost, i2, next_i
                    h[i] = (-best_cost, node, posL, posR)
                # se il nuovo arco a sinistra permette un inserimento migliore di cost, quindi:
                # (best_pos - 1) -- node -- to_ins
                if node not in in_path and adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins] < cost:
                    new_cost = -(adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins])
                    h[i] = (new_cost, node, path[(best_pos - 1) % len(path)], to_ins)
                # se il nuovo arco a destra permette un inserimento migliore di cost, quindi:
                # to_ins -- node -- (best_pos + 1) 
                    best_pos = (best_pos + 1) % (len(path))
                if node not in in_path and adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]] < cost:
                    new_cost = -(adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]])
                    h[i] = (new_cost, node, to_ins, path[(best_pos + 1) % (len(path))])
            heapq.heapify(h)

        self.tour = path
        self.calculateCost()


### Versioni con inizializzazione casuale
        
#@profile
    def nearestInsertionRandomStart(self):
        # inizializzo il path con i due nodi più vicini
        n = self.numCity
        distances = np.array(self.adj)
        path = [random.randint(0, n - 1), random.randint(0, n - 1)]
        while path[0] == path[1]:
            path = [random.randint(0, n - 1), random.randint(0, n - 1)]
        in_path = {path[0], path[1]}
        

        # Inizializza le distanze minime e le città più vicine per ogni città non nel percorso
        h = []
        for i in set(range(n)) - in_path:
            h.append((min(distances[path[0], i], distances[path[1], i]), i))
        heapq.heapify(h)

        while len(path) < n:
            # Trova la città non inserita più vicina a qualsiasi città nel percorso
            _, to_insert = heapq.heappop(h)

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
            for i, (cost, node) in enumerate(h):
                if node not in in_path and distances[to_insert, node] < cost:
                    h[i] = (distances[to_insert, node], node)
            heapq.heapify(h)

        self.tour = path
        self.calculateCost()
    
    def cheapestInsertionRandomStart(self):
        n = self.numCity
        adj = np.array(self.adj)
        path = [random.randint(0, n - 1), random.randint(0, n - 1)]
        while path[0] == path[1]:
            path = [random.randint(0, n - 1), random.randint(0, n - 1)]
        in_path = {path[0], path[1]}
        in_path = {path[0], path[1]}

        h = []
        for i in set(range(n)) - in_path:
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h.append((cost, i, path[0], path[1]))
        heapq.heapify(h)

        while len(path) < n:
            # Trova la città non inserita più vicina a qualsiasi città nel percorso
            (_, to_ins, _, _) = heapq.heappop(h)

            # Trova la posizione ottimale per inserire la città trovata
            best_increase = np.inf
            best_pos = None
            for i in range(len(path)):
                next_i = (i + 1) % len(path)
                increase = adj[path[i], to_ins] + adj[to_ins, path[next_i]] - adj[path[i], path[next_i]]
                if increase < best_increase:
                    best_increase = increase
                    best_pos = next_i

            path.insert(best_pos, to_ins)
            in_path.add(to_ins)

            # A - B - C

            # Aggiorna le distanze minime e le città più vicine per ogni città non nel percorso
            for i, (cost, node, nodeLeft, nodeRight) in enumerate(h):
                # se ho inserito to_ins proprio tra nodeLeft e nodeRight: ricalcolo completamente il costo migliore
                if node not in in_path and nodeLeft == path[(best_pos - 1) % len(path)] and nodeRight == path[(best_pos + 1) % len(path)]:
                    best_cost = np.inf
                    posL, posR = -1, -1
                    for i2 in range(len(path)):
                        next_i = (i2 + 1) % len(path)
                        insertion_cost = adj[path[i2]][node] + adj[node][path[next_i]] - adj[path[i2]][path[next_i]]
                        if best_cost > insertion_cost:
                            best_cost, posL, posR = insertion_cost, i2, next_i
                    h[i] = (best_cost, node, posL, posR)
                # se il nuovo arco a sinistra permette un inserimento migliore di cost, quindi:
                # path[best_pos - 1] -- node -- to_ins
                if node not in in_path and adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins] < cost:
                    new_cost = adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins]
                    h[i] = (new_cost, node, path[(best_pos - 1) % len(path)], to_ins)
                # se il nuovo arco a destra permette un inserimento migliore di cost, quindi:
                # to_ins -- node -- path[best_pos + 1] 
                    best_pos = (best_pos + 1) % (len(path))
                if node not in in_path and adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]] < cost:
                    new_cost = adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]]
                    h[i] = (new_cost, node, to_ins, path[(best_pos + 1) % (len(path))])
            heapq.heapify(h)

        self.tour = path
        self.calculateCost()

    def farthestInsertionRandomStart(self):
        n = self.numCity
        distances = np.array(self.adj)
        path = [random.randint(0, n - 1), random.randint(0, n - 1)]
        while path[0] == path[1]:
            path = [random.randint(0, n - 1), random.randint(0, n - 1)]
        in_path = {path[0], path[1]}
        in_path = {path[0], path[1]}


        # Inizializza le distanze minime e le città più vicine per ogni città non nel percorso
        h = []
        for i in set(range(n)) - in_path:
            h.append((min(distances[path[0], i], distances[path[1], i]), i))
        heapq.heapify(h)

        while len(path) < n:
            # Trova la città non inserita più vicina a qualsiasi città nel percorso
            _, to_insert = heapq.heappop(h)

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
            for i, (cost, node) in enumerate(h):
                cost *= -1
                # cerco comunque di minimizzare distances!
                if node not in in_path and distances[to_insert, node] < cost:
                    h[i] = (-distances[to_insert, node], node)
            heapq.heapify(h)

        self.tour = path
        self.calculateCost()

    def furthestInsertionRandomStart(self):
        n = self.numCity
        adj = np.array(self.adj)
        path = [random.randint(0, n - 1), random.randint(0, n - 1)]
        while path[0] == path[1]:
            path = [random.randint(0, n - 1), random.randint(0, n - 1)]
        in_path = {path[0], path[1]}
        in_path = {path[0], path[1]}

        h = []
        for i in set(range(n)) - in_path:
            adj[path[0]][i]
            adj[i][path[1]]
            adj[path[0]][path[1]]
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h.append((-cost, i, path[0], path[1]))
        heapq.heapify(h)

        while len(path) < n:
            # Trova la città non inserita più vicina a qualsiasi città nel percorso
            (_, to_ins, _, _) = heapq.heappop(h)

            # Trova la posizione ottimale per inserire la città trovata
            best_increase = np.inf
            best_pos = None
            for i in range(len(path)):
                next_i = (i + 1) % len(path)
                increase = adj[path[i], to_ins] + adj[to_ins, path[next_i]] - adj[path[i], path[next_i]]
                if increase < best_increase:
                    best_increase = increase
                    best_pos = next_i

            path.insert(best_pos, to_ins)
            in_path.add(to_ins)

            # Aggiorna le distanze minime e le città più vicine per ogni città non nel percorso
            for i, (cost, node, nodeLeft, nodeRight) in enumerate(h):
                cost *= -1
                # se ho inserito to_ins proprio tra nodeLeft e nodeRight: ricalcolo completamente il costo migliore
                if node not in in_path and nodeLeft == path[(best_pos - 1) % len(path)] and nodeRight == path[(best_pos + 1) % len(path)]:
                    best_cost = np.inf
                    posL, posR = -1, -1
                    for i2 in range(len(path)):
                        next_i = (i2 + 1) % len(path)
                        insertion_cost = adj[path[i2]][node] + adj[node][path[next_i]] - adj[path[i2]][path[next_i]]
                        if best_cost > insertion_cost:
                            best_cost, posL, posR = insertion_cost, i2, next_i
                    h[i] = (-best_cost, node, posL, posR)
                # se il nuovo arco a sinistra permette un inserimento migliore di cost, quindi:
                # (best_pos - 1) -- node -- to_ins
                if node not in in_path and adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins] < cost:
                    new_cost = -(adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins])
                    h[i] = (new_cost, node, path[(best_pos - 1) % len(path)], to_ins)
                # se il nuovo arco a destra permette un inserimento migliore di cost, quindi:
                # to_ins -- node -- (best_pos + 1) 
                    best_pos = (best_pos + 1) % (len(path))
                if node not in in_path and adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]] < cost:
                    new_cost = -(adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]])
                    h[i] = (new_cost, node, to_ins, path[(best_pos + 1) % (len(path))])
            heapq.heapify(h)

        self.tour = path
        self.calculateCost()

soluzioneOttima = {
    "a280" : 2579,
    "ali535" : 202339,
    "att48" : 10628,
    "att532" : 27686,
    "bayg29" : 1610,
    "bays29" : 2020,
    "berlin52" : 7542,
    "bier127" : 118282,
    "brazil58" : 25395,
    "brd14051" : 469385,
    "brg180" : 1950,
    "burma14" : 3323,
    "ch130" : 6110,
    "ch150" : 6528,
    "d198" : 15780,
    "d493" : 35002,
    "d657" : 48912,
    "d1291" : 50801,
    "d1655" : 62128,
    "d2103" : 80450,
    "d15112" : 1573084,
    "d18512" : 645238,
    "dantzig42" : 699,
    "dsj1000" : 18659688,
    "dsj1000" : 18660188,
    "eil51" : 426,
    "eil76" : 538,
    "eil101" : 629,
    "fl417" : 11861,
    "fl1400" : 20127,
    "fl1577" : 22249,
    "fl3795" : 28772,r$ da L, quindi $L = L \setminus \{r\}$.
    "fnl4461" : 182566,
    "fri26" : 937,
    "gil262" : 2378,
    "gr17" : 2085,
    "gr21" : 2707,
    "gr24" : 1272,
    "gr48" : 5046,
    "gr96" : 55209,
    "gr120" : 6942,
    "gr137" : 69853,
    "gr202" : 40160,
    "gr229" : 134602,
    "gr431" : 171414,
    "gr666" : 294358,
    "hk48" : 11461,
    "kroA100" : 21282,
    "kroB100" : 22141,
    "kroC100" : 20749,
    "kroD100" : 21294,
    "kroE100" : 22068,
    "kroA150" : 26524,
    "kroB150" : 26130,
    "kroA200" : 29368,
    "kroB200" : 29437,
    "lin105" : 14379,
    "lin318" : 42029,
    "linhp318" : 41345,
    "nrw1379" : 56638,
    "p654" : 34643,
    "pa561" : 2763,
    "pcb442" : 50778,
    "pcb1173" : 56892,
    "pcb3038" : 137694,
    "pla7397" : 23260728,
    "pla33810" : 66048945,
    "pla85900" : 142382641,
    "pr76" : 108159,
    "pr107" : 44303,
    "pr124" : 59030,
    "pr136" : 96772,
    "pr144" : 58537,
    "pr152" : 73682,
    "pr226" : 80369,
    "pr264" : 49135,
    "pr299" : 48191,
    "pr439" : 107217,
    "pr1002" : 259045,
    "pr2392" : 378032,
    "rat99" : 1211,
    "rat195" : 2323,
    "rat575" : 6773,
    "rat783" : 8806,
    "rd100" : 7910,
    "rd400" : 15281,
    "rl1304" : 252948,
    "rl1323" : 270199,
    "rl1889" : 316536,
    "rl5915" : 565530,
    "rl5934" : 556045,
    "rl11849" : 923288,
    "si175" : 21407,
    "si535" : 48450,
    "si1032" : 92650,
    "st70" : 675,
    "swiss42" : 1273,
    "ts225" : 126643,
    "tsp225" : 3916,
    "u159" : 42080,
    "u574" : 36905,
    "u724" : 41910,
    "u1060" : 224094,
    "u1432" : 152970,
    "u1817" : 57201,
    "u2152" : 64253,
    "u2319" : 234256,
    "ulysses16" : 6859,
    "ulysses22" : 7013,
    "usa13509" : 19982859,
    "vm1084" : 239297,
    "vm1748" : 336556
}
import math
import random
import sys
import numpy as np
import heapq
import matplotlib.pyplot as plt
import numpy as np

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
    
    def cheapestInsertionOn3(self):
        n = self.numCity
        adj = np.array(self.adj)
        path = [0, 0]

        minDist = np.inf
        for i in range(n):
            for j in range(0, i):
                if adj[i][j] < minDist:
                    path[0], path[1] = i, j
                    minDist = adj[i][j]
        in_path = {path[0], path[1]}

        while len(path) < n:
            ln = []
            for v in set(range(n)) - in_path:
                record = [np.inf]
                for i in range(len(path)):
                    l = path[i]
                    r = path[(i + 1) % len(path)]
                    cost = adj[l][v] + adj[v][r] - adj[l][r]
                    if cost < record[0]:
                        record = [cost, v, l, r]
                ln.append(record)
            [_, to_ins, l, r] = min(ln)
            path.insert(path.index(r), to_ins)
            in_path.add(to_ins)                
        self.tour = path
        self.calculateCost()

    
    def cheapestInsertion(self):
        n = self.numCity
        adj = np.array(self.adj)
        path = [0, 0]

        minDist = np.inf
        for i in range(n):
            for j in range(0, i):
                if adj[i][j] < minDist:
                    path[0], path[1] = i, j
                    minDist = adj[i][j]
        in_path = {path[0], path[1]}

        h = []
        for i in set(range(n)) - in_path:
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h.append((cost, i, path[0], path[1]))
        heapq.heapify(h)

        #conteggio = 0
        #tot = 0
        while len(path) < n:
            # Ottieni dallo heap la città che minimizza il minor costo di inserimento
            (costo, to_ins, l, r) = heapq.heappop(h)
            best_pos = path.index(r)
            path.insert(best_pos, to_ins)
            in_path.add(to_ins)

            # Aggiorna le distanze minime e le città più vicine per ogni città non nel percorso
            for i, (cost, node, nodeLeft, nodeRight) in enumerate(h):
                # costo di inserimento di node tra (path[(best_pos - 1) % len(path)], to_ins)
                left_cost = adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins]
                # costo di inserimento di node tra (to_ins, path[(best_pos + 1) % len(path)])
                right_cost = adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]]

                # se ho inserito to_ins proprio tra nodeLeft e nodeRight: ricalcolo completamente il costo migliore
                if node not in in_path and nodeLeft == path[(best_pos - 1) % len(path)] and nodeRight == path[(best_pos + 1) % len(path)]:
                    best_cost = np.inf
                    posL, posR = -1, -1
                    for i2 in range(len(path)):
                        next_i = (i2 + 1) % len(path)
                    #for f in range(best_pos - 3, best_pos + 3):
                    #    i2 = f % len(path)
                        next_i = (i2 + 1) % len(path)
                        insertion_cost = adj[path[i2]][node] + adj[node][path[next_i]] - adj[path[i2]][path[next_i]]
                        if best_cost > insertion_cost:
                            best_cost, posL, posR = insertion_cost, i2, next_i
                    h[i] = (best_cost, node, path[posL], path[posR])
                    (cost, node, nodeLeft, nodeRight) = h[i]
                    #if abs(posR - best_pos) <= 2:
                    #    conteggio += 1
                    
                    #tot += 1
                # se il nuovo arco a sinistra permette un inserimento migliore di cost, quindi:
                # path[best_pos - 1] -- node -- to_ins
                            
                if node not in in_path and left_cost < cost:
                    new_cost = left_cost
                    h[i] = (new_cost, node, path[(best_pos - 1) % len(path)], to_ins)
                    (cost, node, nodeLeft, nodeRight) = h[i]

                # se il nuovo arco a destra permette un inserimento migliore di cost, quindi:
                # to_ins -- node -- path[best_pos + 1] 
                if node not in in_path and right_cost < cost:
                    new_cost = right_cost
                    h[i] = (new_cost, node, to_ins, path[(best_pos + 1) % (len(path))])
            heapq.heapify(h)
        self.tour = path
        self.calculateCost()

        #print(f"{self.name} -> {conteggio / tot}")

    def cheapestInsertionApprossimato(self):
        n = self.numCity
        adj = np.array(self.adj)
        path = [0, 0]

        minDist = np.inf
        for i in range(n):
            for j in range(0, i):
                if adj[i][j] < minDist:
                    path[0], path[1] = i, j
                    minDist = adj[i][j]
        in_path = {path[0], path[1]}

        h = []
        for i in set(range(n)) - in_path:
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h.append((cost, i, path[0], path[1]))
        heapq.heapify(h)

        #conteggio = 0
        #tot = 0
        while len(path) < n:
            # Ottieni dallo heap la città che minimizza il minor costo di inserimento
            (costo, to_ins, l, r) = heapq.heappop(h)
            best_pos = path.index(r)
            path.insert(best_pos, to_ins)
            in_path.add(to_ins)

            # Aggiorna le distanze minime e le città più vicine per ogni città non nel percorso
            for i, (cost, node, nodeLeft, nodeRight) in enumerate(h):
                # costo di inserimento di node tra (path[(best_pos - 1) % len(path)], to_ins)
                left_cost = adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins]
                # costo di inserimento di node tra (to_ins, path[(best_pos + 1) % len(path)])
                right_cost = adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]]

                # se ho inserito to_ins proprio tra nodeLeft e nodeRight: ricalcolo completamente il costo migliore
                if node not in in_path and nodeLeft == path[(best_pos - 1) % len(path)] and nodeRight == path[(best_pos + 1) % len(path)]:
                    best_cost = np.inf
                    posL, posR = -1, -1
                    #for i2 in range(len(path)):
                    #    next_i = (i2 + 1) % len(path)
                    for f in range(best_pos - 3, best_pos + 3):
                        i2 = f % len(path)
                        next_i = (i2 + 1) % len(path)
                        insertion_cost = adj[path[i2]][node] + adj[node][path[next_i]] - adj[path[i2]][path[next_i]]
                        if best_cost > insertion_cost:
                            best_cost, posL, posR = insertion_cost, i2, next_i
                    h[i] = (best_cost, node, path[posL], path[posR])
                    (cost, node, nodeLeft, nodeRight) = h[i]
                    #if abs(posR - best_pos) <= 2:
                    #    conteggio += 1
                    
                    #tot += 1
                # se il nuovo arco a sinistra permette un inserimento migliore di cost, quindi:
                # path[best_pos - 1] -- node -- to_ins
                            
                if node not in in_path and left_cost < cost:
                    new_cost = left_cost
                    h[i] = (new_cost, node, path[(best_pos - 1) % len(path)], to_ins)
                    (cost, node, nodeLeft, nodeRight) = h[i]

                # se il nuovo arco a destra permette un inserimento migliore di cost, quindi:
                # to_ins -- node -- path[best_pos + 1] 
                if node not in in_path and right_cost < cost:
                    new_cost = right_cost
                    h[i] = (new_cost, node, to_ins, path[(best_pos + 1) % (len(path))])
            heapq.heapify(h)
        self.tour = path
        self.calculateCost()

        #print(f"{self.name} -> {conteggio / tot}")

    def cheapestInsertionOttimizzato(self, m):
        n = self.numCity
        adj = np.array(self.adj)
        path = [0, 0]

        minDist = np.inf
        for i in range(n):
            for j in range(0, i):
                if adj[i][j] < minDist:
                    path[0], path[1] = i, j
                    minDist = adj[i][j]
        in_path = {path[0], path[1]}

        # heap principale
        h = []
        # dizionario che associa ogni arco (i, j) nel tour
        # alla lista dei record che puntano all'arco (i, j)
        d = dict()
        d[(path[0], path[1])] = []
        d[(path[1], path[0])] = []
        for i in set(range(n)) - in_path:
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h_i = [cost, i, path[0], path[1]]
            h_i2 = [cost, i, path[1], path[0]]
            h.append([h_i, h_i2])
            d[(path[0], path[1])].append(h_i)
            d[(path[1], path[0])].append(h_i2)
        heapq.heapify(h)

        while len(path) < n:
            # prelevo dallo heap principale lo heap con costo migliore
            h_i = heapq.heappop(h)
            # prelevo dallo heap piccolo del nodo le informazioni utili
            # per inserire to_ins tra (l, r)
            (costo, to_ins, l, r) = heapq.heappop(h_i)
            best_pos = path.index(r)
            path.insert(best_pos, to_ins)
            in_path.add(to_ins)

            for p in d[(l, r)]:
                # cancello i nodi con il riferimento all'arco (l, r)
                # in quanto non esiste più quell'arco
                p[0] = np.inf
            for hp in h:
                node = hp[0][1]

                # sx: path[(best_pos - 1) % len(path)]
                # node
                # dx: path[best_pos]
                sx = path[(best_pos - 1) % len(path)]
                dx = path[best_pos]
                newCost = adj[sx][node] + \
                          adj[node][dx] - \
                          adj[sx][dx]
                l = [newCost, node, sx, dx]
                if (sx, dx) not in d:
                    d[(sx, dx)] = [l]
                else:
                    d[(sx, dx)].append(l)
                hp.append(l)

                # sx: path[best_pos]
                # node
                # dx: path[(best_pos + 1) % len(path)]
                sx = path[best_pos]
                dx = path[(best_pos + 1) % len(path)]
                newCost = adj[sx][node] + \
                          adj[node][dx] - \
                          adj[sx][dx]
                l = [newCost, node, sx, dx]
                if (sx, dx) not in d:
                    d[(sx, dx)] = [l]
                else:
                    d[(sx, dx)].append(l)
                hp.append(l)

                # elimino dallo heap del nodo
                # i riferimenti con costo infinito
                i = 0
                while i < len(hp):
                    if hp[i][0] == np.inf:
                        del hp[i]
                    else:
                        i += 1           
                heapq.heapify(hp)
            # la dimensione massima dello heap del nodo è m
            # quindi rimuovo tutti i nodi da (m+1) in poi
            for i in range(len(h)):
                h[i] = h[i][:m]
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

    def furthestInsertionOn3(self):
        n = self.numCity
        adj = np.array(self.adj)
        path = [0, 0]

        maxDist = 0
        for i in range(n):
            for j in range(0, i):
                if adj[i][j] > maxDist:
                    path[0], path[1] = i, j
                    maxDist = adj[i][j]
        in_path = {path[0], path[1]}

        while len(path) < n:
            ln = []
            for v in set(range(n)) - in_path:
                record = [np.inf]
                for i in range(len(path)):
                    l = path[i]
                    r = path[(i + 1) % len(path)]
                    cost = adj[l][v] + adj[v][r] - adj[l][r]
                    if cost < record[0]:
                        record = [cost, v, l, r]
                ln.append(record)
            [_, to_ins, l, r] = max(ln)
            path.insert(path.index(r), to_ins)
            in_path.add(to_ins)                
        self.tour = path
        self.calculateCost()

    def furthestInsertion(self):
        n = self.numCity
        adj = np.array(self.adj)
        path = [0, 0]

        maxDist = 0
        for i in range(n):
            for j in range(0, i):
                if adj[i][j] > maxDist:
                    path[0], path[1] = i, j
                    maxDist = adj[i][j]
        in_path = {path[0], path[1]}

        h = []
        for i in set(range(n)) - in_path:
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h.append((-cost, i, path[0], path[1]))
        heapq.heapify(h)

        while len(path) < n:
            # Ottieni dallo heap la città che minimizza il minor costo di inserimento
            (_, to_ins, _, r) = heapq.heappop(h)
            best_pos = path.index(r)
            path.insert(best_pos, to_ins)
            in_path.add(to_ins)

            # Aggiorna le distanze minime e le città più vicine per ogni città non nel percorso
            for i, (cost, node, nodeLeft, nodeRight) in enumerate(h):
                cost *= -1
                # costo di inserimento di node tra (path[(best_pos - 1) % len(path)], to_ins)
                left_cost = adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins]
                # costo di inserimento di node tra (to_ins, path[(best_pos + 1) % len(path)])
                right_cost = adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]]

                # se ho inserito to_ins proprio tra nodeLeft e nodeRight: ricalcolo completamente il costo migliore
                if node not in in_path and nodeLeft == path[(best_pos - 1) % len(path)] and nodeRight == path[(best_pos + 1) % len(path)]:
                    best_cost = np.inf
                    posL, posR = -1, -1
                    for i2 in range(len(path)):
                        next_i = (i2 + 1) % len(path)
                    #for f in range(best_pos - 3, best_pos + 3):
                    #    i2 = f % len(path)
                        next_i = (i2 + 1) % len(path)
                        insertion_cost = adj[path[i2]][node] + adj[node][path[next_i]] - adj[path[i2]][path[next_i]]
                        if best_cost > insertion_cost:
                            best_cost, posL, posR = insertion_cost, i2, next_i
                    h[i] = (-best_cost, node, path[posL], path[posR])
                    (cost, node, nodeLeft, nodeRight) = h[i]
                    cost *= -1
                # se il nuovo arco a sinistra permette un inserimento migliore di cost, quindi:
                # path[best_pos - 1] -- node -- to_ins
                            
                if node not in in_path and left_cost < cost:
                    new_cost = left_cost
                    h[i] = (-new_cost, node, path[(best_pos - 1) % len(path)], to_ins)
                    (cost, node, nodeLeft, nodeRight) = h[i]
                    cost *= -1

                # se il nuovo arco a destra permette un inserimento migliore di cost, quindi:
                # to_ins -- node -- path[best_pos + 1] 
                if node not in in_path and right_cost < cost:
                    new_cost = right_cost
                    h[i] = (-new_cost, node, to_ins, path[(best_pos + 1) % (len(path))])
            heapq.heapify(h)
        self.tour = path
        self.calculateCost()

    def furthestInsertionApprossimato(self):
        n = self.numCity
        adj = np.array(self.adj)
        path = [0, 0]

        maxDist = 0
        for i in range(n):
            for j in range(0, i):
                if adj[i][j] > maxDist:
                    path[0], path[1] = i, j
                    maxDist = adj[i][j]
        in_path = {path[0], path[1]}

        h = []
        for i in set(range(n)) - in_path:
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h.append((-cost, i, path[0], path[1]))
        heapq.heapify(h)

        while len(path) < n:
            # Ottieni dallo heap la città che minimizza il minor costo di inserimento
            (_, to_ins, _, r) = heapq.heappop(h)
            best_pos = path.index(r)
            path.insert(best_pos, to_ins)
            in_path.add(to_ins)

            # Aggiorna le distanze minime e le città più vicine per ogni città non nel percorso
            for i, (cost, node, nodeLeft, nodeRight) in enumerate(h):
                cost *= -1
                # costo di inserimento di node tra (path[(best_pos - 1) % len(path)], to_ins)
                left_cost = adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins]
                # costo di inserimento di node tra (to_ins, path[(best_pos + 1) % len(path)])
                right_cost = adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]]

                # se ho inserito to_ins proprio tra nodeLeft e nodeRight: ricalcolo completamente il costo migliore
                if node not in in_path and nodeLeft == path[(best_pos - 1) % len(path)] and nodeRight == path[(best_pos + 1) % len(path)]:
                    best_cost = np.inf
                    posL, posR = -1, -1
                    #for i2 in range(len(path)):
                    #    next_i = (i2 + 1) % len(path)
                    for f in range(best_pos - 3, best_pos + 3):
                        i2 = f % len(path)
                        next_i = (i2 + 1) % len(path)
                        insertion_cost = adj[path[i2]][node] + adj[node][path[next_i]] - adj[path[i2]][path[next_i]]
                        if best_cost > insertion_cost:
                            best_cost, posL, posR = insertion_cost, i2, next_i
                    h[i] = (-best_cost, node, path[posL], path[posR])
                    (cost, node, nodeLeft, nodeRight) = h[i]
                    cost *= -1
                # se il nuovo arco a sinistra permette un inserimento migliore di cost, quindi:
                # path[best_pos - 1] -- node -- to_ins
                            
                if node not in in_path and left_cost < cost:
                    new_cost = left_cost
                    h[i] = (-new_cost, node, path[(best_pos - 1) % len(path)], to_ins)
                    (cost, node, nodeLeft, nodeRight) = h[i]
                    cost *= -1

                # se il nuovo arco a destra permette un inserimento migliore di cost, quindi:
                # to_ins -- node -- path[best_pos + 1] 
                if node not in in_path and right_cost < cost:
                    new_cost = right_cost
                    h[i] = (-new_cost, node, to_ins, path[(best_pos + 1) % (len(path))])
            heapq.heapify(h)
        self.tour = path
        self.calculateCost()

    def furthestInsertionOttimizzato(self, m):
        n = self.numCity
        adj = np.array(self.adj)
        path = [0, 0]

        maxDist = -1
        for i in range(n):
            for j in range(0, i):
                if adj[i][j] > maxDist:
                    path[0], path[1] = i, j
                    maxDist = adj[i][j]
        in_path = {path[0], path[1]}

        h = []
        d = dict()
        d[(path[0], path[1])] = []
        d[(path[1], path[0])] = []
        for i in set(range(n)) - in_path:
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h_i = [-cost, i, path[0], path[1]]
            h_i2 = [-cost, i, path[1], path[0]]
            h.append([h_i, h_i2])
            d[(path[0], path[1])].append(h_i)
            d[(path[1], path[0])].append(h_i2)
        heapq.heapify(h)

        while len(path) < n:
            h_i = heapq.heappop(h)
            (costo, to_ins, l, r) = heapq.heappop(h_i)

            best_pos = path.index(r)
            path.insert(best_pos, to_ins)
            in_path.add(to_ins)

            for p in d[(l, r)]:
                p[0] = np.inf
            for hp in h:
                node = hp[0][1]

                # sx: path[(best_pos - 1) % len(path)]
                # node
                # dx: path[best_pos]
                sx = path[(best_pos - 1) % len(path)]
                dx = path[best_pos]
                newCost = adj[sx][node] + \
                          adj[node][dx] - \
                          adj[sx][dx]
                l = [newCost, node, sx, dx]
                if (sx, dx) not in d:
                    d[(sx, dx)] = [l]
                else:
                    d[(sx, dx)].append(l)
                hp.append(l)

                # sx: path[best_pos]
                # node
                # dx: path[(best_pos + 1) % len(path)]
                sx = path[best_pos]
                dx = path[(best_pos + 1) % len(path)]
                newCost = adj[sx][node] + \
                          adj[node][dx] - \
                          adj[sx][dx]
                l = [newCost, node, sx, dx]
                if (sx, dx) not in d:
                    d[(sx, dx)] = [l]
                else:
                    d[(sx, dx)].append(l)
                hp.append(l)

                i = 0
                # riporto i costi negati a positivi
                for p in hp:
                    if p[0] < 0:
                        p[0] *= -1
                while i < len(hp):
                    if hp[i][0] == np.inf:
                        del hp[i]
                    else:
                        i += 1
                # ora lo heap mantiene i costi migliori (più bassi)    
                heapq.heapify(hp)
                # converto solo il costo migliore (più basso) ad
                # un valore negativo: in questo modo lo heap principale
                # opera come max-heap
                hp[0][0] *= -1
            for i in range(len(h)):
                h[i] = h[i][:m]
            # ottengo la struttura max-heap
            # solo il primo record ha costo negativo
            heapq.heapify(h)
        self.tour = path
        self.calculateCost()


### Versioni con inizializzazione casuale
    def nearestNeighborRandomStart(self):
        self.tour = [random.randint(0, self.numCity - 1)]
        visited = set([self.tour[0]])
        notVisited = set(range(0, self.numCity)) - set([self.tour[0]])
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

        h = []
        for i in set(range(n)) - in_path:
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h.append((cost, i, path[0], path[1]))
        heapq.heapify(h)

        while len(path) < n:
            # Ottieni dallo heap la città che minimizza il minor costo di inserimento
            (_, to_ins, _, pos) = heapq.heappop(h)
            best_pos = path.index(pos)
            path.insert(best_pos, to_ins)
            in_path.add(to_ins)

            # Aggiorna le distanze minime e le città più vicine per ogni città non nel percorso
            for i, (cost, node, nodeLeft, nodeRight) in enumerate(h):
                # costo di inserimento di node tra (path[(best_pos - 1) % len(path)], to_ins)
                left_cost = adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins]
                # costo di inserimento di node tra (to_ins, path[(best_pos + 1) % len(path)])
                right_cost = adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]]

                # se ho inserito to_ins proprio tra nodeLeft e nodeRight: ricalcolo completamente il costo migliore
                if node not in in_path and nodeLeft == path[(best_pos - 1) % len(path)] and nodeRight == path[(best_pos + 1) % len(path)]:
                    best_cost = np.inf
                    posL, posR = -1, -1
                    for i2 in range(len(path)):
                        next_i = (i2 + 1) % len(path)
                        insertion_cost = adj[path[i2]][node] + adj[node][path[next_i]] - adj[path[i2]][path[next_i]]
                        if best_cost > insertion_cost:
                            best_cost, posL, posR = insertion_cost, i2, next_i
                    h[i] = (best_cost, node, path[posL], path[posR])
                    (cost, node, nodeLeft, nodeRight) = h[i]
                # se il nuovo arco a sinistra permette un inserimento migliore di cost, quindi:
                # path[best_pos - 1] -- node -- to_ins
                            
                if node not in in_path and left_cost < cost:
                    new_cost = left_cost
                    h[i] = (new_cost, node, path[(best_pos - 1) % len(path)], to_ins)
                    (cost, node, nodeLeft, nodeRight) = h[i]

                # se il nuovo arco a destra permette un inserimento migliore di cost, quindi:
                # to_ins -- node -- path[best_pos + 1] 
                if node not in in_path and right_cost < cost:
                    new_cost = right_cost
                    h[i] = (new_cost, node, to_ins, path[(best_pos + 1) % (len(path))])
            heapq.heapify(h)
        self.tour = path
        self.calculateCost()

    def cheapestInsertionOttimizzatoRandomStart(self, m):
        n = self.numCity
        adj = np.array(self.adj)
        path = [random.randint(0, n - 1), random.randint(0, n - 1)]
        while path[0] == path[1]:
            path = [random.randint(0, n - 1), random.randint(0, n - 1)]
        in_path = {path[0], path[1]}

        # heap principale
        h = []
        # dizionario che associa ogni arco (i, j) nel tour
        # alla lista dei record che puntano all'arco (i, j)
        d = dict()
        d[(path[0], path[1])] = []
        d[(path[1], path[0])] = []
        for i in set(range(n)) - in_path:
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h_i = [cost, i, path[0], path[1]]
            h_i2 = [cost, i, path[1], path[0]]
            h.append([h_i, h_i2])
            d[(path[0], path[1])].append(h_i)
            d[(path[1], path[0])].append(h_i2)
        heapq.heapify(h)

        while len(path) < n:
            # prelevo dallo heap principale lo heap con costo migliore
            h_i = heapq.heappop(h)
            # prelevo dallo heap piccolo del nodo le informazioni utili
            # per inserire to_ins tra (l, r)
            (costo, to_ins, l, r) = heapq.heappop(h_i)
            best_pos = path.index(r)
            path.insert(best_pos, to_ins)
            in_path.add(to_ins)

            for p in d[(l, r)]:
                # cancello i nodi con il riferimento all'arco (l, r)
                # in quanto non esiste più quell'arco
                p[0] = np.inf
            for hp in h:
                node = hp[0][1]

                # sx: path[(best_pos - 1) % len(path)]
                # node
                # dx: path[best_pos]
                sx = path[(best_pos - 1) % len(path)]
                dx = path[best_pos]
                newCost = adj[sx][node] + \
                          adj[node][dx] - \
                          adj[sx][dx]
                l = [newCost, node, sx, dx]
                if (sx, dx) not in d:
                    d[(sx, dx)] = [l]
                else:
                    d[(sx, dx)].append(l)
                hp.append(l)

                # sx: path[best_pos]
                # node
                # dx: path[(best_pos + 1) % len(path)]
                sx = path[best_pos]
                dx = path[(best_pos + 1) % len(path)]
                newCost = adj[sx][node] + \
                          adj[node][dx] - \
                          adj[sx][dx]
                l = [newCost, node, sx, dx]
                if (sx, dx) not in d:
                    d[(sx, dx)] = [l]
                else:
                    d[(sx, dx)].append(l)
                hp.append(l)

                # elimino dallo heap del nodo
                # i riferimenti con costo infinito
                i = 0
                while i < len(hp):
                    if hp[i][0] == np.inf:
                        del hp[i]
                    else:
                        i += 1           
                heapq.heapify(hp)
            # la dimensione massima dello heap del nodo è m
            # quindi rimuovo tutti i nodi da (m+1) in poi
            for i in range(len(h)):
                h[i] = h[i][:m]
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

        h = []
        for i in set(range(n)) - in_path:
            cost = adj[path[0]][i] + adj[i][path[1]] - adj[path[0]][path[1]]
            h.append((-cost, i, path[0], path[1]))
        heapq.heapify(h)

        while len(path) < n:
            # Ottieni dallo heap la città che minimizza il minor costo di inserimento
            (_, to_ins, _, pos) = heapq.heappop(h)
            best_pos = path.index(pos)
            path.insert(best_pos, to_ins)
            in_path.add(to_ins)

            # Aggiorna le distanze minime e le città più vicine per ogni città non nel percorso
            for i, (cost, node, nodeLeft, nodeRight) in enumerate(h):
                cost *= -1
                # costo di inserimento di node tra (path[(best_pos - 1) % len(path)], to_ins)
                left_cost = adj[path[(best_pos - 1) % len(path)]][node] + adj[node][to_ins] - adj[path[(best_pos - 1) % len(path)]][to_ins]
                # costo di inserimento di node tra (to_ins, path[(best_pos + 1) % len(path)])
                right_cost = adj[to_ins][node] + adj[node][path[(best_pos + 1) % (len(path))]] - adj[to_ins][path[(best_pos + 1) % (len(path))]]

                # se ho inserito to_ins proprio tra nodeLeft e nodeRight: ricalcolo completamente il costo migliore
                if node not in in_path and nodeLeft == path[(best_pos - 1) % len(path)] and nodeRight == path[(best_pos + 1) % len(path)]:
                    best_cost = np.inf
                    posL, posR = -1, -1
                    for i2 in range(len(path)):
                        next_i = (i2 + 1) % len(path)
                        insertion_cost = adj[path[i2]][node] + adj[node][path[next_i]] - adj[path[i2]][path[next_i]]
                        if best_cost > insertion_cost:
                            best_cost, posL, posR = insertion_cost, i2, next_i
                    h[i] = (-best_cost, node, path[posL], path[posR])
                    (cost, node, nodeLeft, nodeRight) = h[i]
                    cost *= -1
                # se il nuovo arco a sinistra permette un inserimento migliore di cost, quindi:
                # path[best_pos - 1] -- node -- to_ins
                            
                if node not in in_path and left_cost < cost:
                    new_cost = left_cost
                    h[i] = (-new_cost, node, path[(best_pos - 1) % len(path)], to_ins)
                    (cost, node, nodeLeft, nodeRight) = h[i]
                    cost *= -1

                # se il nuovo arco a destra permette un inserimento migliore di cost, quindi:
                # to_ins -- node -- path[best_pos + 1] 
                if node not in in_path and right_cost < cost:
                    new_cost = right_cost
                    h[i] = (-new_cost, node, to_ins, path[(best_pos + 1) % (len(path))])
            heapq.heapify(h)
        self.tour = path
        self.calculateCost()

    # sceglie casualmente il nodo da inserire e lo inserisce casualmente
    def randomInsertion2(self):
        tour = []
        notInTour = [x for x in range(self.numCity)]
        random.shuffle(notInTour)
        for i in notInTour:
            tour.insert(random.randint(0, len(tour) - 1), i)
        self.tour = tour
        self.calculateCost()

    def randomInsertion(self):
        # sceglie casualmente il nodo da inserisce MA lo inserisce nel modo migliore possibile (minimizzando l'inserimento)
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

### Metodi per mostrare a schermo il tour
    def showGraphWithTour(self, path):
        # "chiudo" il ciclo aggiungendo il ritorno al primo nodo
        tour = path + [path[0]]
        xpoints = np.array([self.coord[x][0] for x in tour])
        ypoints = np.array([self.coord[x][1] for x in tour])

        xpoints = xpoints + [xpoints[0]]
        ypoints = ypoints + [ypoints[0]]

        plt.plot(xpoints, ypoints)
        plt.scatter(xpoints, ypoints)
        plt.show()

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
    "fl3795" : 28772,   
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
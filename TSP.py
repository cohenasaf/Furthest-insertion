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
                    best_position = i + 1

            path.insert(best_position, to_insert)
            in_path.add(to_insert)

        self.tour = path
        self.calculateCost()

        
    #@profile
    def nearestNeighbor(self):
        self.tour = [0]
        visited = set()
        visited.add(0)
        while len(self.tour) < self.numCity:
            cost = sys.maxsize
            j = -1
            for j2 in set(x for x in range(self.numCity)) - visited:
                if self.adj[self.tour[-1]][j2] < cost:
                    cost = self.adj[self.tour[-1]][j2]
                    j = j2
            self.tour.append(j)
            visited.add(j)
        self.calculateCost()
    
    #@profile
    def nearestInsertion(self):
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
        n = self.numCity
        dist = self.adj
        tour = [0, 0]

        minCost = np.inf
        for i in range(1, n):
            if dist[0][i] < minCost:
                minCost = dist[0][i]
                tour[1] = i
        inTour = {tour[0], tour[1]}
        notInTour = {x for x in range(n)} - {tour[0], tour[1]}

        # h rappresenta la coda con priorità dove il costo è la priorità,
        # mantiene informazioni come: il nodo da aggiungere i e
        # i due nodi nei quali si inserisce i
        h = []
        for i in notInTour:
            cost = dist[tour[0]][i] + dist[i][tour[1]] - dist[tour[0]][tour[1]]
            h.append((cost, i, tour[0], tour[1]))
        heapq.heapify(h)

        while len(tour) < n:
            (_, insert, intoLeft, intoRight) = heapq.heappop(h)
            if insert in inTour:
                # il nodo è già stato inserito
                continue
            for pos, _ in enumerate(tour):
                if tour[pos] == intoRight:
                    tour.insert(pos, insert)
                    break
            inTour.add(tour[pos])
            notInTour.remove(tour[pos]) 
            
            # aggiorno i costi nello heap in base alla modifica del tour: considero solo il punto del tour modificato (attorno a insert)
            for pos, (cost, i, _, _) in enumerate(h):
                if cost > dist[intoLeft][i] + dist[i][insert] - dist[intoLeft][insert]:
                    # intoLeft i insert
                    h[pos] = (dist[intoLeft][i] + dist[i][insert] - dist[intoLeft][insert], i, intoLeft, insert)
                if cost > dist[insert][i] + dist[i][intoRight] - dist[insert][intoRight]:
                    # insert i intoRight
                    h[pos] = (dist[insert][i] + dist[i][intoRight] - dist[insert][intoRight], i, insert, intoRight)
            # ricrea l'albero dopo le modifiche => O(log(n))
            heapq.heapify(h)

        self.tour = tour
        self.calculateCost()

    #@profile
    def farthestInsertion(self):
        n = self.numCity
        distances = np.array(self.adj)
        path = [0]  # Inizia da una città arbitraria, in questo caso la prima
        in_path = {0}
        max_distance_to_path = np.zeros(n, dtype=int)
        farthest_city_to_path = np.zeros(n, dtype=int)

        # Inizializza le distanze minime e le città più vicine per ogni città non nel percorso
        for i in range(1, n):
            max_distance_to_path[i] = distances[0, i]
            farthest_city_to_path[i] = 0

        while len(path) < n:
            # Trova la città non inserita più vicina a qualsiasi città nel percorso
            to_insert = np.argmax(max_distance_to_path)
            max_distance_to_path[to_insert] = 0

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
                if i not in in_path and distances[to_insert, i] > max_distance_to_path[i]:
                    max_distance_to_path[i] = distances[to_insert, i]
                    farthest_city_to_path[i] = to_insert

        self.tour = path
        self.calculateCost()

    #@profile
    def furthestInsertion(self):
        n = self.numCity
        dist = self.adj
        tour = [0, 0]

        minCost = np.inf
        for i in range(1, n):
            if dist[0][i] < minCost:
                minCost = dist[0][i]
                tour[1] = i
        inTour = {tour[0], tour[1]}
        notInTour = {x for x in range(n)} - {tour[0], tour[1]}

        # h rappresenta la coda con priorità dove il costo è la priorità,
        # mantiene informazioni come: il nodo da aggiungere i e
        # i due nodi nei quali si inserisce i
        h = []
        for i in notInTour:
            cost = dist[tour[0]][i] + dist[i][tour[1]] - dist[tour[0]][tour[1]]
            h.append((-cost, i, tour[0], tour[1]))
        heapq.heapify(h)

        while len(tour) < n:
            (_, insert, intoLeft, intoRight) = heapq.heappop(h)
            if insert in inTour:
                # il nodo è già stato inserito
                continue
            for pos, _ in enumerate(tour):
                if tour[pos] == intoRight:
                    tour.insert(pos, insert)
                    break
            inTour.add(tour[pos])
            notInTour.remove(tour[pos]) 
            
            # aggiorno i costi nello heap in base alla modifica del tour: considero solo il punto del tour modificato (attorno a insert)
            for pos, (cost, i, _, _) in enumerate(h):
                # riconverto il costo in un valore positivo
                cost *= -1
                if cost > dist[intoLeft][i] + dist[i][insert] - dist[intoLeft][insert]:
                    # intoLeft i insert
                    h[pos] = (-(dist[intoLeft][i] + dist[i][insert] - dist[intoLeft][insert]), i, intoLeft, insert)
                if cost > dist[insert][i] + dist[i][intoRight] - dist[insert][intoRight]:
                    # insert i intoRight
                    h[pos] = (-(dist[insert][i] + dist[i][intoRight] - dist[insert][intoRight]), i, insert, intoRight)
            # ricrea l'albero dopo le modifiche => O(log(n))
            heapq.heapify(h)

        self.tour = tour
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
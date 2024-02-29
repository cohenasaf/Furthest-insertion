import math

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
        coord = []
        for line in f:
            if "EOF" in line:
                break
            if data:
                line = line.replace("  ", " ").replace("  ", " ").replace("\n", "").strip()
                coord.append([int(line.split(" ")[1]), int(line.split(" ")[2])])
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
                    self.adj[i][j] = self.adj[j][i] = self.distance(coord[i], coord[j])

        # leggo il persorso ottimale
        f = open(f"ALL-TSP/{name}.opt.tour")
        self.optTour = [-1 for _ in range(self.numCity)]
        self.Tour = [-1 for _ in range(self.numCity)]
        data = False
        i = 0
        for line in f:
            if "-1" in line:
                break
            if data:
                self.optTour[i] = int(line)
                i += 1
            if "TOUR_SECTION" in line:
                data = True
        f.close()
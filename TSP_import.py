import math

def create_matrix(rows, cols, value=0):
    return [[value for _ in range(cols)] for _ in range(rows)]

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def openTSP(name):
    # estraggo i dati delle coordinate euclidee
    f = open(f"ALL-TSP/{name}.tsp")
    numCity = -1
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
            numCity = int(line.split(": ")[1])
        if "NODE_COORD_SECTION" in line:
            data = True
    f.close()

    adj = create_matrix(numCity, numCity)
    for i in range(numCity):
        for j in range(i):
            if i == j:
                continue
            else:
                adj[i][j] = adj[j][i] = distance(coord[i], coord[j])

    # leggo il persorso ottimale
    f = open(f"ALL-TSP/{name}.opt.tour")
    optTour = [-1 for _ in range(numCity)]
    data = False
    i = 0
    for line in f:
        if "-1" in line:
            break
        if data:
            optTour[i] = int(line)
            i += 1
        if "TOUR_SECTION" in line:
            data = True
    print(optTour)
    print(len(optTour))
    f.close()
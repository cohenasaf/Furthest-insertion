import math
"""
import glob
listTSP = glob.glob("ALL-TSP/*")

for file in listTSP:
    f = open(file)
    print(f.read())
    print("ciaone")
    f.close()
"""

# Decisioni che ho preso:
# i costi float li ho trasformati in interi moltiplicandoli per 100 e togliendo la virgola
f = open("ALL-TSP/a280.tsp")
ok = False
coord = []
for line in f:
    if "EOF" in line:
        break
    if ok:
        nums = line.strip().replace("  ", " ").replace("  ", " ").split(" ")
        coord.append([int(nums[1]), int(nums[2])])
    if "NODE_COORD_SECTION" in line:
        ok = True
f.close()

adj = [[len(coord)*i+j for j in range(len(coord))] for i in range(len(coord))]

for pos1, p1 in enumerate(coord):
    for pos2, p2 in enumerate(coord):
        if pos1 == pos2:
            adj[pos1][pos2] = 0
        else:
            adj[pos1][pos2] = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

f = open("grafi casuali/0", "w")
f.write(str(len(coord)))
f.write(" ")
for i in adj:
    for j in i:
        f.write(str(round(j * 100)))
        f.write(" ")
f.close()

f = open("ALL-TSP/a280.opt.tour")
f2 = open("grafi casuali/0.opt", "w")
ok = False
for line in f:
    if ok:
        f2.write(line.replace("\n", ""))
        f2.write(" ")
    if "TOUR_SECTION" in line:
        ok = True
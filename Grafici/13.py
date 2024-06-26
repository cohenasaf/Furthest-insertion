import matplotlib.pyplot as plt
import numpy as np

l = [('eil51', 1), ('berlin52', 1), ('st70', 2), ('pr76', 1), ('eil76', 1), ('rat99', 1), ('kroD100', 3), ('kroA100', 1), ('kroC100', 1), ('kroB100', 1), ('kroE100', 1), ('rd100', 1), ('eil101', 1), ('lin105', 1), ('pr107', 3), ('pr124', 3), ('bier127', 2), ('ch130', 3), ('pr136', 1), ('pr144', 3), ('kroA150', 3), ('ch150', 1), ('kroB150', 3), ('pr152', 1), ('u159', 3), ('rat195', 1), ('d198', 3), ('kroA200', 1), ('kroB200', 3), ('ts225', 2), ('tsp225', 3), ('pr226', 1), ('gil262', 1), ('pr264', 3), ('a280', 1), ('pr299', 2), ('lin318', 3), ('linhp318', 3), ('rd400', 3), ('fl417', 1), ('pr439', 2), ('pcb442', 3), ('d493', 1), ('u574', 3), ('rat575', 3), ('p654', 3), ('d657', 3), ('u724', 3), ('rat783', 3), ('pr1002', 2)]
dF = {'eil51': 3, 'berlin52': 3, 'st70': 3, 'pr76': 3, 'eil76': 5, 'rat99': 3, 'kroD100': 3, 'kroA100': 3, 'kroC100': 3, 'kroB100': 3, 'kroE100': 3, 'rd100': 3, 'eil101': 5, 'lin105': 3, 'pr107': 3, 'pr124': 3, 'bier127': 6, 'ch130': 3, 'pr136': 3, 'pr144': 3, 'kroA150': 5, 'ch150': 4, 'kroB150': 3, 'pr152': 3, 'u159': 3, 'rat195': 5, 'd198': 6, 'kroA200': 5, 'kroB200': 3, 'ts225': 6, 'tsp225': 4, 'pr226': 3, 'gil262': 6, 'pr264': 6, 'a280': 6, 'pr299': 3, 'lin318': 5, 'linhp318': 5, 'rd400': 6, 'fl417': 3, 'pr439': 6, 'pcb442': 6, 'd493': 6, 'u574': 6, 'rat575': 5, 'p654': 3, 'd657': 6, 'u724': 6, 'rat783': 6, 'pr1002': 6}

# Sample data (4 lists)
x = [x[0] for x in l[:50]]

y1 = [np.float64(1.0863505068255777), np.float64(1.1174669409080433), np.float64(1.0745455105256998), np.float64(1.0718878443105828), np.float64(1.1017309842508243), np.float64(1.115768966415897), np.float64(1.0853389375543172), np.float64(1.081253290147963), np.float64(1.0895788498030101), np.float64(1.0816816363550443), np.float64(1.0745617059268195), np.float64(1.098253290544059), np.float64(1.1139426237356154), np.float64(1.1025036845854836), np.float64(1.032364031796134), np.float64(1.0820818630559645), np.float64(1.1204067209150708), np.float64(1.093993720001844), np.float64(1.0835123334377164), np.float64(1.076165033601214), np.float64(1.0915434891907203), np.float64(1.1085046419471751), np.float64(1.0867088930224724), np.float64(1.0602918125397591), np.float64(1.1200931464190311), np.float64(1.1411498962563635), np.float64(1.0664942374412896), np.float64(1.0974051850817372), np.float64(1.0981615766888284), np.float64(1.1328084608734637), np.float64(1.0999411113067992), np.float64(1.049180621684143), np.float64(1.1131575132118006), np.float64(1.1121134247822289), np.float64(1.1642284667202067), np.float64(1.1183056923371835), np.float64(1.1101604002601304), np.float64(1.1252426401917188), np.float64(1.1110336746131961), np.float64(1.078123048106765), np.float64(1.1296085328810237), np.float64(1.1442931011945552), np.float64(1.1061594942260984), np.float64(1.1189133779700606), np.float64(1.1283372097168956), np.float64(1.0649818606541825), np.float64(1.1194426206686545), np.float64(1.1253834698811802), np.float64(1.135877527054933), np.float64(1.1260850970762164)]
y2 = [np.float64(3.888103546967358), np.float64(3.9833420132488557), np.float64(5.432497648239745), np.float64(5.289877097695537), np.float64(4.7030349433759735), np.float64(7.0015963107776455), np.float64(7.630774212804503), np.float64(7.997110556748105), np.float64(8.197596455062072), np.float64(7.657338279433095), np.float64(7.8584218577375715), np.float64(7.058504228149915), np.float64(5.467872779520104), np.float64(8.518066451036201), np.float64(13.051659329026704), np.float64(11.833324093337648), np.float64(5.325486420530467), np.float64(7.533042110352386), np.float64(8.500510253211445), np.float64(13.913722467278458), np.float64(9.659522505807642), np.float64(8.319935902922651), np.float64(9.852107239117153), np.float64(14.161062751994523), np.float64(10.709028319400787), np.float64(9.789410720613061), np.float64(12.08756682117475), np.float64(11.596866130803033), np.float64(11.29839789495322), np.float64(12.604736340213288), np.float64(10.531035851825628), np.float64(20.97924842884596), np.float64(11.237701304423972), np.float64(22.822835056176242), np.float64(13.217708587023735), np.float64(15.716529070178222), np.float64(13.96235790859434), np.float64(14.155522177758785), np.float64(13.790104995958657), np.float64(41.8812475059164), np.float64(17.77866315203295), np.float64(15.227840897497538), np.float64(12.797321855381348), np.float64(18.460268828195254), np.float64(16.822233350396676), np.float64(58.7291709153979), np.float64(17.4824461384266), np.float64(20.8030845029215), np.float64(20.337965008007856), np.float64(24.918706193103212)]
#print(np.mean(y1))
#print(np.mean(y2))
#print(np.mean(y3))
#print(np.mean(y4))
#print(np.mean(y5))
#exit()

# qualità Furthest

# Plotting each list with different color and marker
plt.figure(figsize=(14, 6))

plt.plot(x, y1, marker='o', color='blue', label='Random Insertion')
plt.plot(x, y2, marker='s', color='red', label='Random Insertion 2')
plt.xticks(rotation=45)
plt.xlabel('Prime 50 istanze TSP da TSP-LIB')
plt.ylabel('Media delle qualità trovate')
plt.yscale('log')
plt.title('Media delle qualità trovate')
plt.legend()  # Show legend based on labels

plt.grid(True)
plt.tight_layout()
plt.savefig("/home/asaf/Desktop/Furthest-insertion/Grafici/13.png")
plt.show()


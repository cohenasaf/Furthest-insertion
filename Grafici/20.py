import matplotlib.pyplot as plt
import numpy as np

#l = [('eil51', 1), ('berlin52', 1), ('st70', 2), ('pr76', 1), ('eil76', 1), ('rat99', 1), ('kroD100', 3), ('kroA100', 1), ('kroC100', 1), ('kroB100', 1), ('kroE100', 1), ('rd100', 1), ('eil101', 1), ('lin105', 1), ('pr107', 3), ('pr124', 3), ('bier127', 2), ('ch130', 3), ('pr136', 1), ('pr144', 3), ('kroA150', 3), ('ch150', 1), ('kroB150', 3), ('pr152', 1), ('u159', 3), ('rat195', 1), ('d198', 3), ('kroA200', 1), ('kroB200', 3), ('ts225', 2), ('tsp225', 3), ('pr226', 1), ('gil262', 1), ('pr264', 3), ('a280', 1), ('pr299', 2), ('lin318', 3), ('linhp318', 3), ('rd400', 3), ('fl417', 1), ('pr439', 2), ('pcb442', 3), ('d493', 1), ('u574', 3), ('rat575', 3), ('p654', 3), ('d657', 3), ('u724', 3), ('rat783', 3), ('pr1002', 2)]
#dF = {'eil51': 3, 'berlin52': 3, 'st70': 3, 'pr76': 3, 'eil76': 5, 'rat99': 3, 'kroD100': 3, 'kroA100': 3, 'kroC100': 3, 'kroB100': 3, 'kroE100': 3, 'rd100': 3, 'eil101': 5, 'lin105': 3, 'pr107': 3, 'pr124': 3, 'bier127': 6, 'ch130': 3, 'pr136': 3, 'pr144': 3, 'kroA150': 5, 'ch150': 4, 'kroB150': 3, 'pr152': 3, 'u159': 3, 'rat195': 5, 'd198': 6, 'kroA200': 5, 'kroB200': 3, 'ts225': 6, 'tsp225': 4, 'pr226': 3, 'gil262': 6, 'pr264': 6, 'a280': 6, 'pr299': 3, 'lin318': 5, 'linhp318': 5, 'rd400': 6, 'fl417': 3, 'pr439': 6, 'pcb442': 6, 'd493': 6, 'u574': 6, 'rat575': 5, 'p654': 3, 'd657': 6, 'u724': 6, 'rat783': 6, 'pr1002': 6}

TSP_LIB = ['eil51', 'berlin52', 'st70', 'pr76', 'eil76', 'rat99', 'kroD100', 'kroA100', 'kroC100', 'kroB100', 'kroE100', 'rd100', 'eil101', 'lin105', 'pr107', 'pr124', 'bier127', 'ch130', 'pr136', 'pr144', 'kroA150', 'ch150', 'kroB150', 'pr152', 'u159', 'rat195', 'd198', 'kroA200', 'kroB200', 'ts225', 'tsp225', 'pr226', 'gil262', 'pr264', 'a280', 'pr299', 'lin318', 'linhp318', 'rd400', 'fl417', 'pr439', 'pcb442', 'd493', 'u574', 'rat575', 'p654', 'd657', 'u724', 'rat783', 'pr1002', 'u1060', 'vm1084', 'pcb1173', 'd1291', 'rl1304', 'rl1323', 'nrw1379', 'fl1400', 'u1432', 'fl1577', 'd1655', 'vm1748', 'u1817', 'rl1889', 'd2103', 'u2152', 'u2319', 'pr2392', 'pcb3038', 'fl3795', 'fnl4461', 'rl5915', 'rl5934', 'rl11849', 'usa13509', 'brd14051', 'd15112', 'd18512']


# Sample data (4 lists)
x = [str(x) for x in range(50, 100)]

y1 = [np.float64(760.0), np.float64(767.25), np.float64(790.875), np.float64(786.05), np.float64(806.0), np.float64(799.325), np.float64(791.2), np.float64(810.875), np.float64(820.6), np.float64(845.875), np.float64(841.275), np.float64(853.1), np.float64(842.675), np.float64(860.775), np.float64(877.55), np.float64(863.3), np.float64(892.0), np.float64(891.575), np.float64(918.325), np.float64(900.025), np.float64(905.375), np.float64(919.15), np.float64(927.75), np.float64(925.525), np.float64(949.55), np.float64(946.55), np.float64(964.3), np.float64(937.875), np.float64(967.525), np.float64(986.8), np.float64(969.35), np.float64(1006.95), np.float64(972.25), np.float64(1004.95), np.float64(1001.4), np.float64(1010.4), np.float64(1015.075), np.float64(1025.15), np.float64(1018.925), np.float64(1006.9), np.float64(1050.475), np.float64(1027.575), np.float64(1052.25), np.float64(1073.175), np.float64(1068.2), np.float64(1073.525), np.float64(1090.8), np.float64(1104.0), np.float64(1080.9), np.float64(1098.175)]
y2 = [np.float64(787.725), np.float64(798.5), np.float64(816.825), np.float64(808.975), np.float64(826.925), np.float64(820.425), np.float64(813.125), np.float64(839.725), np.float64(848.35), np.float64(871.5), np.float64(886.275), np.float64(901.05), np.float64(877.525), np.float64(895.75), np.float64(917.15), np.float64(903.85), np.float64(929.85), np.float64(944.85), np.float64(957.475), np.float64(945.5), np.float64(949.5), np.float64(954.25), np.float64(970.3), np.float64(971.925), np.float64(1002.55), np.float64(994.525), np.float64(1020.225), np.float64(996.9), np.float64(1006.975), np.float64(1029.875), np.float64(1014.125), np.float64(1063.875), np.float64(1037.5), np.float64(1071.9), np.float64(1045.925), np.float64(1067.525), np.float64(1075.375), np.float64(1082.1), np.float64(1083.175), np.float64(1071.625), np.float64(1100.625), np.float64(1095.775), np.float64(1132.85), np.float64(1143.2), np.float64(1135.425), np.float64(1149.775), np.float64(1162.725), np.float64(1168.825), np.float64(1158.15), np.float64(1170.1)]
y3 = [np.float64(788.45), np.float64(798.5), np.float64(817.575), np.float64(812.9), np.float64(834.625), np.float64(831.475), np.float64(815.875), np.float64(848.525), np.float64(850.1), np.float64(878.3), np.float64(883.85), np.float64(901.2), np.float64(886.575), np.float64(893.1), np.float64(919.975), np.float64(910.875), np.float64(933.3), np.float64(940.375), np.float64(956.725), np.float64(954.75), np.float64(955.175), np.float64(959.8), np.float64(971.775), np.float64(984.925), np.float64(999.65), np.float64(996.175), np.float64(1003.85), np.float64(997.2), np.float64(1021.75), np.float64(1036.775), np.float64(1024.3), np.float64(1063.55), np.float64(1043.15), np.float64(1076.9), np.float64(1059.675), np.float64(1072.75), np.float64(1084.65), np.float64(1096.5), np.float64(1087.125), np.float64(1070.575), np.float64(1114.1), np.float64(1094.7), np.float64(1142.3), np.float64(1143.125), np.float64(1140.45), np.float64(1163.5), np.float64(1175.1), np.float64(1179.0), np.float64(1168.25), np.float64(1164.4)]
y4 = [np.float64(800.275), np.float64(799.775), np.float64(812.4), np.float64(816.05), np.float64(836.85), np.float64(836.775), np.float64(835.125), np.float64(856.075), np.float64(853.925), np.float64(886.35), np.float64(889.175), np.float64(910.175), np.float64(887.675), np.float64(909.2), np.float64(939.45), np.float64(912.375), np.float64(938.325), np.float64(954.225), np.float64(958.95), np.float64(961.25), np.float64(963.625), np.float64(965.425), np.float64(987.2), np.float64(991.875), np.float64(1005.5), np.float64(1013.15), np.float64(1024.45), np.float64(1018.275), np.float64(1034.6), np.float64(1050.4), np.float64(1033.675), np.float64(1061.425), np.float64(1044.65), np.float64(1078.925), np.float64(1068.175), np.float64(1095.225), np.float64(1099.675), np.float64(1109.05), np.float64(1086.925), np.float64(1079.425), np.float64(1115.975), np.float64(1101.3), np.float64(1146.275), np.float64(1151.5), np.float64(1155.325), np.float64(1163.15), np.float64(1169.275), np.float64(1192.825), np.float64(1174.65), np.float64(1187.525)]
y5 = [np.float64(795.725), np.float64(800.5), np.float64(813.575), np.float64(816.175), np.float64(836.05), np.float64(822.45), np.float64(818.95), np.float64(848.825), np.float64(848.675), np.float64(881.0), np.float64(887.425), np.float64(905.85), np.float64(892.675), np.float64(894.675), np.float64(929.65), np.float64(913.95), np.float64(931.525), np.float64(954.775), np.float64(972.975), np.float64(941.825), np.float64(968.75), np.float64(971.55), np.float64(977.85), np.float64(972.725), np.float64(1003.275), np.float64(1011.7), np.float64(1036.675), np.float64(998.375), np.float64(1018.5), np.float64(1046.4), np.float64(1033.25), np.float64(1078.55), np.float64(1046.225), np.float64(1082.65), np.float64(1049.225), np.float64(1081.1), np.float64(1086.825), np.float64(1095.875), np.float64(1100.1), np.float64(1078.55), np.float64(1112.85), np.float64(1098.45), np.float64(1139.575), np.float64(1155.3), np.float64(1141.5), np.float64(1160.8), np.float64(1161.45), np.float64(1184.75), np.float64(1160.675), np.float64(1178.45)]

#print(np.mean(y1))
#print(np.mean(y2))
#print(np.mean(y3))
#print(np.mean(y4))
#print(np.mean(y5))
#exit()

# qualità Furthest

# Plotting each list with different color and marker
plt.figure(figsize=(14, 6))

plt.plot(x, y1, marker='o', color='blue', label='Nearest Neighbor')
plt.plot(x, y2, marker='s', color='red', label='Nearest Insertion')
plt.plot(x, y3, marker='d', color='purple', label='Cheapest Insertion versione 3')
plt.plot(x, y4, marker='^', color='green', label='Farthest Insertion')
plt.plot(x, y5, marker='*', color='orange', label='Furthest Insertion versione 2')

plt.xticks(rotation=45)
plt.xlabel(f'Dimensione dell\'istanza')
plt.ylabel('Qualità media per ogni dimensione')
#plt.yscale('log')
plt.title('Qualità media per ogni dimensione dell\'istanza generata casualmente')
plt.legend()  # Show legend based on labels

plt.grid(True)
plt.tight_layout()
plt.savefig("/home/asaf/Desktop/Furthest-insertion/Grafici/20.png")
plt.show()


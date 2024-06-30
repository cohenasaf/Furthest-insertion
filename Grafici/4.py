l = [('eil51', 1), ('berlin52', 1), ('st70', 2), ('pr76', 1), ('eil76', 1), ('rat99', 1), ('kroD100', 3), ('kroA100', 1), ('kroC100', 1), ('kroB100', 1), ('kroE100', 1), ('rd100', 1), ('eil101', 1), ('lin105', 1), ('pr107', 3), ('pr124', 3), ('bier127', 2), ('ch130', 3), ('pr136', 1), ('pr144', 3), ('kroA150', 3), ('ch150', 1), ('kroB150', 3), ('pr152', 1), ('u159', 3), ('rat195', 1), ('d198', 3), ('kroA200', 1), ('kroB200', 3), ('ts225', 2), ('tsp225', 3), ('pr226', 1), ('gil262', 1), ('pr264', 3), ('a280', 1), ('pr299', 2), ('lin318', 3), ('linhp318', 3), ('rd400', 3), ('fl417', 1), ('pr439', 2), ('pcb442', 3), ('d493', 1), ('u574', 3), ('rat575', 3), ('p654', 3), ('d657', 3), ('u724', 3), ('rat783', 3), ('pr1002', 2)]
#dF = {'eil51': 3, 'berlin52': 3, 'st70': 3, 'pr76': 3, 'eil76': 5, 'rat99': 3, 'kroD100': 3, 'kroA100': 3, 'kroC100': 3, 'kroB100': 3, 'kroE100': 3, 'rd100': 3, 'eil101': 5, 'lin105': 3, 'pr107': 3, 'pr124': 3, 'bier127': 6, 'ch130': 3, 'pr136': 3, 'pr144': 3, 'kroA150': 5, 'ch150': 4, 'kroB150': 3, 'pr152': 3, 'u159': 3, 'rat195': 5, 'd198': 6, 'kroA200': 5, 'kroB200': 3, 'ts225': 6, 'tsp225': 4, 'pr226': 3, 'gil262': 6, 'pr264': 6, 'a280': 6, 'pr299': 3, 'lin318': 5, 'linhp318': 5, 'rd400': 6, 'fl417': 3, 'pr439': 6, 'pcb442': 6, 'd493': 6, 'u574': 6, 'rat575': 5, 'p654': 3, 'd657': 6, 'u724': 6, 'rat783': 6, 'pr1002': 6}
dF = {'eil51': 3, 'berlin52': 3, 'st70': 3, 'pr76': 3, 'eil76': 6, 'rat99': 3, 'kroD100': 3, 'kroA100': 3, 'kroC100': 3, 'kroB100': 3, 'kroE100': 3, 'rd100': 3, 'eil101': 6, 'lin105': 3, 'pr107': 3, 'pr124': 3, 'bier127': 6, 'ch130': 6, 'pr136': 3, 'pr144': 3, 'kroA150': 7, 'ch150': 6, 'kroB150': 3, 'pr152': 3, 'u159': 3, 'rat195': 7, 'd198': 3, 'kroA200': 6, 'kroB200': 3, 'ts225': 6, 'tsp225': 6, 'pr226': 3, 'gil262': 6, 'pr264': 6, 'a280': 6, 'pr299': 3, 'lin318': 6, 'linhp318': 6, 'rd400': 7, 'fl417': 3, 'pr439': 7, 'pcb442': 6, 'd493': 10, 'u574': 7, 'rat575': 7, 'p654': 3, 'd657': 7, 'u724': 7, 'rat783': 7, 'pr1002': 7}

import matplotlib.pyplot as plt

# Supponiamo di avere 50 label chiamate 'label_0', 'label_1', ..., 'label_49'
#labels = [x[0] for x in l]
labels = [x for x in dF.keys()]
#numeri_associati = [x[1] for x in l]  # Supponendo che i numeri aumentino con la posizione
numeri_associati = [x for x in dF.values()]  # Supponendo che i numeri aumentino con la posizione

# Creare il grafico
plt.figure(figsize=(16, 6))
plt.bar(labels, numeri_associati)
plt.xlabel('Label')
plt.ylabel('Parametro m minimo')
plt.xticks(rotation=45)  # Ruota le label sull'asse x di 45 gradi
plt.grid(axis='y')  # Mostra la griglia solo sull'asse y
plt.savefig("/home/asaf/Desktop/Furthest-insertion/Grafici/4.png", format="png")
plt.show()
l = [('eil51', 1), ('berlin52', 1), ('st70', 2), ('pr76', 1), ('eil76', 1), ('rat99', 1), ('kroD100', 3), ('kroA100', 1), ('kroC100', 1), ('kroB100', 1), ('kroE100', 1), ('rd100', 1), ('eil101', 1), ('lin105', 1), ('pr107', 3), ('pr124', 3), ('bier127', 2), ('ch130', 3), ('pr136', 1), ('pr144', 3), ('kroA150', 3), ('ch150', 1), ('kroB150', 3), ('pr152', 1), ('u159', 3), ('rat195', 1), ('d198', 3), ('kroA200', 1), ('kroB200', 3), ('ts225', 2), ('tsp225', 3), ('pr226', 1), ('gil262', 1), ('pr264', 3), ('a280', 1), ('pr299', 2), ('lin318', 3), ('linhp318', 3), ('rd400', 3), ('fl417', 1), ('pr439', 2), ('pcb442', 3), ('d493', 1), ('u574', 3), ('rat575', 3), ('p654', 3), ('d657', 3), ('u724', 3), ('rat783', 3), ('pr1002', 2)]
dC = {'eil51': 1, 'berlin52': 1, 'st70': 3, 'pr76': 1, 'eil76': 1, 'rat99': 1, 'kroD100': 3, 'kroA100': 1, 'kroC100': 1, 'kroB100': 1, 'kroE100': 1, 'rd100': 1, 'eil101': 1, 'lin105': 1, 'pr107': 3, 'pr124': 2, 'bier127': 3, 'ch130': 2, 'pr136': 1, 'pr144': 3, 'kroA150': 2, 'ch150': 1, 'kroB150': 2, 'pr152': 1, 'u159': 3, 'rat195': 1, 'd198': 2, 'kroA200': 1, 'kroB200': 3, 'ts225': 3, 'tsp225': 3, 'pr226': 1, 'gil262': 1, 'pr264': 3, 'a280': 1, 'pr299': 2, 'lin318': 2, 'linhp318': 2, 'rd400': 3, 'fl417': 1, 'pr439': 3, 'pcb442': 3, 'd493': 1, 'u574': 3, 'rat575': 3, 'p654': 3, 'd657': 2, 'u724': 2, 'rat783': 3, 'pr1002': 2}

import matplotlib.pyplot as plt

labels = [x for x in dC.keys()]
numeri_associati = [x for x in dC.values()] 

plt.figure(figsize=(16, 6))
plt.bar(labels, numeri_associati)
plt.xlabel('Label')
plt.ylabel('Parametro m minimo')
plt.xticks(rotation=45) 
plt.grid(axis='y')
plt.savefig("/home/asaf/Desktop/Furthest-insertion/Grafici/1.png", format="png")
plt.show()
l = [('eil51', 1), ('berlin52', 1), ('st70', 2), ('pr76', 1), ('eil76', 1), ('rat99', 1), ('kroD100', 3), ('kroA100', 1), ('kroC100', 1), ('kroB100', 1), ('kroE100', 1), ('rd100', 1), ('eil101', 1), ('lin105', 1), ('pr107', 3), ('pr124', 3), ('bier127', 2), ('ch130', 3), ('pr136', 1), ('pr144', 3), ('kroA150', 3), ('ch150', 1), ('kroB150', 3), ('pr152', 1), ('u159', 3), ('rat195', 1), ('d198', 3), ('kroA200', 1), ('kroB200', 3), ('ts225', 2), ('tsp225', 3), ('pr226', 1), ('gil262', 1), ('pr264', 3), ('a280', 1), ('pr299', 2), ('lin318', 3), ('linhp318', 3), ('rd400', 3), ('fl417', 1), ('pr439', 2), ('pcb442', 3), ('d493', 1), ('u574', 3), ('rat575', 3), ('p654', 3), ('d657', 3), ('u724', 3), ('rat783', 3), ('pr1002', 2)]


import matplotlib.pyplot as plt

# Supponiamo di avere 50 label chiamate 'label_0', 'label_1', ..., 'label_49'
labels = [x[0] for x in l]
numeri_associati = [x[1] for x in l]  # Supponendo che i numeri aumentino con la posizione

# Creare il grafico
plt.figure(figsize=(12, 6))
plt.bar(labels, numeri_associati)
plt.xlabel('Label')
plt.ylabel('Parametro m minimo')
plt.xticks(rotation=45)  # Ruota le label sull'asse x di 45 gradi
plt.grid(axis='y')  # Mostra la griglia solo sull'asse y
plt.savefig("riCIO.png", format="png")
plt.show()
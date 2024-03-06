import numpy as np

def calculate_distances(cities):
    """Calcola la matrice delle distanze tra tutte le coppie di città."""
    n = len(cities)
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            distance = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
            distances[i, j] = distances[j, i] = distance
    return distances

def nearest_insertion_optimized(cities):
    n = len(cities)
    distances = calculate_distances(cities)
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

    return path

# Esempio di utilizzo
cities = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2)]  # Esempio di coordinate delle città
path = nearest_insertion_optimized(cities)
print("Percorso:", path)

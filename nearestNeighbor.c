/*
Nearest Neighbor è una euristica costruttiva greedy per il problema del TSP
Complessità Temporale: O(n^2)
Complessità Spaziale: O(n) // contando solo l'array visited e tour
La soluzione trovata può essere anche molto lontana dall'ottimo
*/

void nearestNeighbor() {
    // inizializzo tutti i vertici come non visitati
    for (int i = 0; i < numCities; i++) visited[i] == 0;
    // scelgo un vertice casuale
    int current = rand() % numCities;
    // lo imposto come visitato
    visited[current] = 1;
    // e lo considero come il primo nel tour
    tour[0] = current;
    lenTour++;


    for (int i = 1; i < numCities; i++) {
        int nearestCity = -1;
        int minDistance = INT_MAX;

        // cerco il nodo nearestCity più vicino al nodo current (tra i non visitati)
        for (int j = 0; j < numCities; j++) {
            if (!visited[j] && adjacencyMatrix[current][j] < minDistance) {
                nearestCity = j;
                minDistance = adjacencyMatrix[current][j];
            }
        }

        // lo imposto come visitato, lo aggiungo al ciclo, imposto il nuovo nodo come current
        visited[nearestCity] = 1;
        tour[i] = nearestCity;
        current = nearestCity;
        lenTour++;
    }

    // Aggiungiamo il ritorno al nodo di partenza
    tour[numCities] = tour[0];
    cost = tourCost();
}
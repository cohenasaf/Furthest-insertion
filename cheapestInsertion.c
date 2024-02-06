/*
Nearest Insertion è una euristica costruttiva per il problema del TSP
*/

//#include "graphGenerator.c"


void cheapestInsertion() {
    cost = 0;
    // inizializzo tutti i vertici come non visitati
    for (int i = 0; i < numCities; i++) visited[i] == 0;
    // inizializzo il subtour con la coppia di vertici con costo minore
    int minDistance = INT_MAX;
    for (int i = 0; i < numCities; i++) {
        for (int j = 0; j < numCities; j++) {
            if (adjacencyMatrix[i][j] < minDistance) {
                tour[0] = i;
                tour[1] = j;
            }
        }
    }
    visited[tour[0]] = 1;
    visited[tour[1]] = 1;
    lenTour = 2;

    int r;
    while(lenTour < numCities) {
        int minCost = INT_MAX, i, j;
        for (int k = 0; k < lenTour - 1; k++) {
            for (int r = 0; r < numCities; r++) {
                printf("%d\n", lenTour);
                cost = adjacencyMatrix[tour[k]][r] + adjacencyMatrix[r][tour[k + 1]] - adjacencyMatrix[tour[k]][tour[k + 1]];
                if (!visited[r] && cost < minCost) {
                    minCost = cost;
                    i = tour[k];
                    j = tour[k + 1];
                }
            }
        }
        insertNode(r, i, j);
        visited[r] = 1;
        lenTour++;
    }
    // aggiungo l'ultima città non visitata
    for (int r = 0; r < numCities; r++) {
        if (!visited[r]) {
            tour[numCities - 1] = r;
            break;
        }
    }
    cost = tourCost();
}
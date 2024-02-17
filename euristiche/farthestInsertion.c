/*
Farthest Insertion è una euristica costruttiva per il problema del TSP
*/

//#include "graphGenerator.c"


void farthestInsertion() {
    cost = 0;
    // inizializzo tutti i vertici come non visitati
    for (int i = 0; i < numCities; i++) visited[i] == 0;
    // inizializzo il subtour con la coppia di vertici con costo minore
    int minDistance = INT_MAX;
    for (int i = 0; i < lenTour; i++) {
        for (int j = 0; j < lenTour; j++) {
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
        // Passo di selezione: scelgo il nodo r NON ancora visitato
        // tale che abbia distanza minima con un qualunque nodo j
        minDistance = 0;
        int j;
        for (int r2 = 0; r2 < numCities; r2++) {
            for (int j2 = 0; j2 < numCities; j2++) {
                if (!visited[r2] && visited[j2]  && adjacencyMatrix[r2][j2] > minDistance) {
                    minDistance = adjacencyMatrix[r2][j2];
                    r = r2;
                }
            }
        }
        //printf("j: %d, r: %d\n", j, r);

        // scelgo l'arco (i, j) nel subtour in modo da minimizzare c_ir + c_rj - c_ij 
        int i, minCost = INT_MAX;
        for (int k = 0; k < lenTour - 1; k++) {
            int cost = adjacencyMatrix[tour[k]][r] + adjacencyMatrix[r][tour[k + 1]] - adjacencyMatrix[tour[i]][tour[k + 1]];
            if (cost < minCost) {
                minCost = cost;
                i = tour[k];
                j = tour[k + 1];
            } 
        }
        //printf("i: %d\n", i);
        // inserisco il nodo r nel ciclo e lo imposto come visitato
        insertNode(r, i, j);
        visited[r] = 1;
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
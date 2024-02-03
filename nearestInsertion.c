/*
Nearest Insertion è una euristica costruttiva per il problema del TSP
*/

//#include "graphGenerator.c"


void nearestInsertion() {
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
        minDistance = INT_MAX;
        int j;
        for (int r2 = 0; r2 < numCities; r2++) {
            if (visited[r2]) continue;
            int j2;
            for (j2 = 0; j2 < numCities; j2++) {
                if (!visited[j2] || r2 == j2) {
                    continue;
                }
                if (adjacencyMatrix[r2][j2] < minDistance) {
                    minDistance = adjacencyMatrix[r2][j2];
                    j = j2;
                    r = r2;
                }
            }
        }
        //printf("j: %d, r: %d\n", j, r);

        // scelgo l'arco (i, j) in modo da minimizzare c_ir + c_rj - c_ij 
        int i;
        for (int k = 0; k < lenTour; k++) {
            if (tour[k] == j) {
                if (k == 0) {
                    if (tour[k + 1] == r) continue;
                    i = tour[k + 1];
                } else if (k == lenTour - 1) {
                    if (tour[k - 1] == r) continue;
                    i = tour[k - 1];
                } else {
                    int i1 = tour[k + 1];
                    int i2 = tour[k - 1];
                    int d1 = adjacencyMatrix[i1][r] + adjacencyMatrix[r][j] - adjacencyMatrix[i1][j];
                    int d2 = adjacencyMatrix[i2][r] + adjacencyMatrix[r][j] - adjacencyMatrix[i2][j];
                    if (i1 == r) i = i2;
                    else if (i2 == r) i = i1;
                    if (d1 < d2) {
                        i = i1;
                    } else {
                        i = i2;
                    }
                }
                break;
            }
        }
        //printf("i: %d\n", i);
        // inserisco il nodo r nel ciclo e lo imposto come visitato
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
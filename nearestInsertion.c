/*
Nearest Insertion è una euristica costruttiva per il problema del TSP
*/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

#define MAX_CITIES 20000

int numCities;
int adjacencyMatrix[MAX_CITIES][MAX_CITIES];
int tour[MAX_CITIES];
int visited[MAX_CITIES];
int lenTour = 0;

// Genera un grafo non orientato casuale, vale 0 <= (i, j) < 100
void generateRandomMatrix(int numCities, int adjacencyMatrix[MAX_CITIES][MAX_CITIES]) {
    srand(time(NULL));
    for (int i = 0; i < numCities; i++) {
        for (int j = i + 1; j < numCities; j++) {
            if (i == j) {
                adjacencyMatrix[i][i] = 0; // Nessun costo da una città a se stessa
            } else {
                int random = rand() % 100;
                adjacencyMatrix[i][j] = random; // Peso casuale tra 0 e 100 escluso
                adjacencyMatrix[j][i] = random; // Matrice simmetrica
            }
        }
    }
}

// inserisce il nodo r tra i e j
void insertNode(int r, int i, int j) {
    for (int k = 0; k < lenTour; k++) {
        if (tour[k] == i || tour[k] == j) {
            for (int q = lenTour - 1; q > k; q--) {
                tour[q + 1] = tour[q];
            }
            tour[k + 1] = r;
            return;
        }
    }
    return;
}

void nearestInsertion() {
    // inizializzo tutti i vertici come non visitati
    for (int i = 0; i < numCities; i++) visited[i] == 0;
    // scelgo il primo vertice casualmente
    tour[0] = rand() % numCities;
    // lo imposto come visitato
    visited[tour[0]] = 1;
    // imposto la lunghezza del sub-tour

    int r = -1;
    int minDistance = INT_MAX;

    // cerco il nodo r più vicino a current 
    for (int i = 0; i < numCities; i++) {
        if (r != i && adjacencyMatrix[tour[0]][i] < minDistance) {
            r = i;
            minDistance = adjacencyMatrix[tour[0]][i];
        }
    }

    // lo imposto come visitato
    visited[tour[1]] = 1;
    tour[1] = r;
    lenTour = 2;

    while(lenTour < numCities - 1) {
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

        // scelgo l'arco (i, j) in modo da minimizzare c_ir + c_rj - c_ij 
        int i;
        for (int k = 0; k < lenTour; k++) {
            if (tour[k] == j) {
                if (k == 0) {
                    i = tour[k + 1];
                } else if (k == lenTour - 1) {
                    i = tour[k - 1];
                } else {
                    int i1 = tour[k + 1];
                    int i2 = tour[k - 1];
                    int d1 = adjacencyMatrix[i1][r] + adjacencyMatrix[r][j] - adjacencyMatrix[i1][j];
                    int d2 = adjacencyMatrix[i2][r] + adjacencyMatrix[r][j] - adjacencyMatrix[i2][j];
                    if (d1 < d2) {
                        i = i1;
                    } else {
                        i = i2;
                    }
                }
                break;
            }
        }
        // inserisco il nodo r nel ciclo e lo imposto come visitato
        insertNode(r, i, j);
        visited[r] = 1;
        lenTour++;
    }
    // aggiungo l'ultima città non visitata
    for (int r = 0; r < numCities; r++) {
        if (!visited[r]) {
            tour[numCities - 1] = r;
            tour[numCities] = tour[0];
            break;
        }
    }
}

void printMatrix() {
    printf("La matrice casuale è:\n");
    for (int i = 0; i < numCities; i++) {
        for (int j = 0; j < numCities; j++) {
            printf("%.2d ", adjacencyMatrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    printf("Inserisci il numero di città: ");
    scanf("%d", &numCities);

    generateRandomMatrix(numCities, adjacencyMatrix);

    if (numCities < 30) printMatrix();
    
    clock_t t; 
    t = clock(); 

    nearestInsertion();

    t = clock() - t; 
    double time_taken = ((double)t)/CLOCKS_PER_SEC;
 
    printf("Tour ottimale: ");
    for (int i = 0; i <= numCities; i++) {
        printf("%d ", tour[i]);
    }
    printf("\n");

    printf("nearestNeighbor() took %f seconds to execute \n", time_taken); 

    return 0;
}

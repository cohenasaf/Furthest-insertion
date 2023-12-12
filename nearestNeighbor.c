/*
Nearest Neighbor è una euristica costruttiva greedy per il problema del TSP
Complessità Temporale: O(n^2)
Complessità Spaziale: O(n) // contando solo l'array visited e tour
La soluzione trovata può essere anche molto lontana dall'ottimo
*/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

#define MAX_CITIES 20000

int numCities;
int adjacencyMatrix[MAX_CITIES][MAX_CITIES];
int visited[MAX_CITIES];
int tour[MAX_CITIES];

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

// https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm
void nearestNeighbor() {
    // inizializzo tutti i vertici come non visitati
    for (int i = 0; i < numCities; i++) visited[i] == 0;
    // scelgo un vertice casuale
    int current = rand() % numCities;
    // lo imposto come visitato
    visited[current] = 1;
    // e lo considero come il primo nel tour
    tour[0] = current;

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
    }

    // Aggiungiamo il ritorno al nodo di partenza
    tour[numCities] = tour[0];
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

    for (int i = 0; i < numCities; i++) {
        visited[i] = 0;
    }

    clock_t t;
    t = clock(); 

    nearestNeighbor();

    t = clock() - t; 
    double time_taken = ((double)t)/CLOCKS_PER_SEC;
 
    printf("Tour ottimale: ");
    for (int i = 0; i <= numCities; i++) {
        printf("%d ", tour[i]);
    }
    printf("\n");

    printf("Tempo di esecuzione dell'euristica NearestNeighbor: %f secondi.\n", time_taken); 

    return 0;
}

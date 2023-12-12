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
int lenTour = 2;

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

void nearestInsertion() {
    // inizializzo tutti i vertici come non visitati
    for (int i = 0; i < numCities; i++) visited[i] == 0;
    // scelgo il primo vertice casualmente
    tour[0] = rand() % numCities;
    // lo imposto come visitato
    visited[tour[0]] = 1;

    int r = -1;
    int minDistance = INT_MAX;

    // cerco il nodo r più vicino a current 
    for (int i = 0; i < numCities; i++) {
        if (r != i && adjacencyMatrix[tour[0]][i] < minDistance) {
            r = i;
            minDistance = adjacencyMatrix[tour[0]][i];
        }
    }

    visited[tour[1]] = 1;
    tour[1] = r;

    // COMPLETARE CON LE LISTE CONCATENATE



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

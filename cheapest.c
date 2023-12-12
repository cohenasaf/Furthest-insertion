#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

#define MAX_CITIES 100

int numCities;
int adjacencyMatrix[MAX_CITIES][MAX_CITIES];
int visited[MAX_CITIES];
int tour[MAX_CITIES];

void generateRandomMatrix(int numCities, int adjacencyMatrix[MAX_CITIES][MAX_CITIES]) {
    srand(time(NULL));

    for (int i = 0; i < numCities; i++) {
        for (int j = 0; j < numCities; j++) {
            if (i == j) {
                adjacencyMatrix[i][j] = 0; // Nessun costo da una città a se stessa
            } else {
                adjacencyMatrix[i][j] = rand() % 100; // Peso casuale tra 0 e 100 escluso
            }
        }
    }
}

void nearestNeighbor(int start) {
    int current = start;
    visited[current] = 1;
    tour[0] = current;

    for (int i = 1; i < numCities; i++) {
        int nearestCity = -1;
        int minDistance = INT_MAX;

        for (int j = 0; j < numCities; j++) {
            if (!visited[j] && adjacencyMatrix[current][j] < minDistance) {
                nearestCity = j;
                minDistance = adjacencyMatrix[current][j];
            }
        }

        visited[nearestCity] = 1;
        tour[i] = nearestCity;
        current = nearestCity;
    }

    // Aggiungiamo il ritorno al nodo di partenza
    tour[numCities] = start;
}

void printMatrix() {
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
    printf("La matrice casuale è:\n");
    printMatrix();

    for (int i = 0; i < numCities; i++) {
        visited[i] = 0;
    }

    int startingCity;
    printf("Inserisci la città di partenza (da 0 a %d): ", numCities - 1);
    scanf("%d", &startingCity);

    nearestNeighbor(startingCity);

    printf("Tour ottimale: ");
    for (int i = 0; i <= numCities; i++) {
        printf("%d ", tour[i]);
    }

    printf("\n");

    return 0;
}

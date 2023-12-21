#include "euristicTest.h"
#include "nearestInsertion.c"
#include "nearestNeighbor.c"
#include <stdio.h>

#define MAX_CITIES 20000

int numCities;
int adjacencyMatrix[MAX_CITIES][MAX_CITIES];
int tour[MAX_CITIES];
int visited[MAX_CITIES];
int lenTour = 0;
int cost = 0;

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

void writeMatrixOnFile(File *fptr) {
    fprintf(fptr, "%d\n", numCities);
    for (int i = 0; i < numCities; i++) {
        for (int j = 0; j < numCities; j++) {
            fprintf(fptr, "%d ", adjacencyMatrix[i][j]);
        }
        fprintf(fptr, "\n");
    }
}


int main() {
    FILE *fptr;
    fptr = fopen("filename.txt", "w");
    //fprintf(fptr, "Some text");
    fclose(fptr);
    return 0;
}
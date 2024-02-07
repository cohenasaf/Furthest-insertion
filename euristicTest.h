/*
Breve libreria che consente di generare le matrici casuali, testare l'euristica proposta, valutare le prestazioni
*/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
#include <sys/time.h>

#define MAX_CITIES 20000

int numCities;
int adjacencyMatrix[MAX_CITIES][MAX_CITIES];
int tour[MAX_CITIES];
int visited[MAX_CITIES];
int lenTour = 0;
int cost = 0;

int tourCost() {
    int cost = 0;
    for (int i = 0; i < lenTour - 1; i++) {
        cost += adjacencyMatrix[tour[i]][tour[i + 1]];
    }
    cost += adjacencyMatrix[tour[lenTour - 1]][tour[0]];
    return cost;
}

// genera il seed basato su nanosecondi, utile per generare molte matrici casuali piccole
unsigned int ottieni_seed() {
    struct timeval tempo_corrente;
    gettimeofday(&tempo_corrente, NULL);
    unsigned int seed = tempo_corrente.tv_sec * 1000000 + tempo_corrente.tv_usec;
    return seed;
}

// Genera un grafo non orientato casuale, vale 0 <= (i, j) < 100
void generateRandomMatrix(int numCities, int adjacencyMatrix[MAX_CITIES][MAX_CITIES]) {
    srand(ottieni_seed());
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
            lenTour++;
            return;
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

void printTour() {
    printf("Il tour è: ");
    for (int i = 0; i < lenTour; i++) printf("%d ", tour[i]);
    printf("\n");
}

void clearDataStructures() {
    for (int i = 0; i < MAX_CITIES; i++) {
        tour[i] = 0;
        visited[i] = 0;
    }
    lenTour = 0;
    cost = 0;
}

double testEuristicTime(int n, void (*e)()) {
    clearDataStructures();
    numCities = n;

    //generateRandomMatrix(numCities, adjacencyMatrix);

    //if (numCities < 30) printMatrix();
    
    clock_t t; 
    t = clock(); 

    (*e)();

    t = clock() - t; 
    return ((double)t)/CLOCKS_PER_SEC;
}

void testEuristicCost(int n, void (*e)()) {
    numCities = n;

    //generateRandomMatrix(numCities, adjacencyMatrix);
    clearDataStructures();
    //if (numCities < 30) printMatrix();
    
    (*e)();
}

int isHamiltonianCycle() {
    for (int i = 0; i < lenTour; i++) {
        int a = 0;
        for (int j = 0; j < lenTour; j++) {
            if (tour[i] == j) {
                a = 1;
                break;
            }
        }
        if (a == 0) {
            return 0;
        }
    }
    return 1;
}

int hasTourDuplicates() {
    for (int i = 0; i < lenTour; i++) {
        for (int j = i + 1; j < lenTour; j++) {
            if (tour[i] == tour[j]) {
                return 1;
            }
        }
    }
    return 0;
}
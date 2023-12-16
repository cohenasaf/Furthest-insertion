#include "linkedList.h"

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

#define MAX_CITIES 20000

int numCities;
int adjacencyMatrix[MAX_CITIES][MAX_CITIES];
int tour[MAX_CITIES];
int visited[MAX_CITIES];
int lenTour = 20;

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

int main() {
    for (int i = 0; i < 20; i++) tour[i] = i;
    insertNode(500, 6, 5);
    for (int i = 0; i < 21; i++) {
        printf("%d ", tour[i]);
    }
    printf("\n");
}
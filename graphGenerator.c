#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "euristicTest.h"

// il primo numero indica il numero di città
// gli altri sono la matrice in ordine (prima riga,
// seconda riga...)
void writeRandomGraphFile(char *title, int n) {
    numCities = n;
    char folder[20] = "grafi casuali/";
    FILE* file = fopen(strcat(folder, title), "w");
    fprintf(file, "%d ", n);
    generateRandomMatrix(numCities, adjacencyMatrix);
    for (int i = 0; i < numCities; i++) {
        for (int j = 0; j < numCities; j++) {
            fprintf(file, "%d ", adjacencyMatrix[i][j]);
        }
    }
    fclose(file);
}

// legge il file e importa in adjacencyMatrix la matrice
void readRandomGraphFile(char *title) {
    char folder[] = "grafi casuali/";

    FILE *file = fopen(strcat(folder, title), "r");
    size_t n = 0;
    int c;

    if (file == NULL) {
        printf("Errore lettura file");
        return;
    }
    
    int first = 0, i = 0;
    char *numero = malloc(3);
    while ((c = fgetc(file)) != EOF) {
        n = 0;
        numero[n++] = (char) c;
        while ((c = fgetc(file)) != ' ') {
            numero[n++] = (char) c;
        }
        numero[n++] = '\0';
        int num = atoi(numero);

        if (first == 0) {
            numCities = num;
            first = 1;
        } else {
            adjacencyMatrix[i / numCities][i % numCities] = num;
            i++;
        }
    }
    fclose(file);
}

// genera n matrici casuali grandi c città
void generaNMatriciCasuali(int n, int c) {
    for (int i = 0; i < n; i++) {
        char name[10];
        sprintf(name, "%d", i);
        writeRandomGraphFile(name, c);
        printf("Generata la matrice casuale %d ...\n", i);
    }
}

int main(int argc, char **argv) {
    generaNMatriciCasuali(100, 1000);
}
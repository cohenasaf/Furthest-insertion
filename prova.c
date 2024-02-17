#include <stdio.h>

// Definizione della struttura edge
struct edge {
    int primo;
    int secondo;
    int terzo;
};

// Funzione per scambiare due elementi
void scambia(struct edge *a, struct edge *b) {
    struct edge temp = *a;
    *a = *b;
    *b = temp;
}

// Funzione di partizionamento per QuickSort
int partiziona(struct edge arr[], int basso, int alto) {
    // Pivot - elemento di partizione
    int pivot = arr[alto].terzo;
    int i = (basso - 1); // Indice dell'elemento più piccolo

    for (int j = basso; j <= alto - 1; j++) {
        // Se l'elemento corrente è più piccolo o uguale al pivot
        if (arr[j].terzo <= pivot) {
            i++; // incrementa l'indice dell'elemento più piccolo
            scambia(&arr[i], &arr[j]);
        }
    }
    scambia(&arr[i + 1], &arr[alto]);
    return (i + 1);
}

// Funzione principale per eseguire il QuickSort
void quickSort(struct edge arr[], int basso, int alto) {
    if (basso < alto) {
        // pi è l'indice di partizionamento, arr[pi] è ora al posto giusto
        int pi = partiziona(arr, basso, alto);

        // Ordina separatamente gli elementi prima e dopo il partizionamento
        quickSort(arr, basso, pi - 1);
        quickSort(arr, pi + 1, alto);
    }
}

// Funzione per stampare un array di edge
void stampaArray(struct edge arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("{%d, %d, %d}\n", arr[i].primo, arr[i].secondo, arr[i].terzo);
    }
    printf("\n");
}

int main() {
    struct edge arr[] = {{1, 5, -2}, {4, 1, 30}, {7, 8, 9}, {2, 3, 1}};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Array non ordinato:\n");
    stampaArray(arr, n);

    quickSort(arr, 0, n-1);

    printf("Array ordinato in base al terzo intero:\n");
    stampaArray(arr, n);

    return 0;
}

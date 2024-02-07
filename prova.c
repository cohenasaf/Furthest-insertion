#include <time.h>
#include <stdio.h>

void permute(int array[], int start, int end) {
    array[1] = 200;
}

int main() {
    //int array[] = {1, 2, 3, 4, 5}; 
    int array[] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++) printf("%d ", array[i]);
    printf("\n");
    permute(array, 1, 2);
    for (int i = 0; i < 5; i++) printf("%d ", array[i]);
    printf("\n");
}
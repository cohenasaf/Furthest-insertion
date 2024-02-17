//#include "graphGenerator.c"

int tempTour[MAX_CITIES];

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void permute(int array[], int start, int end) {
    if (start == end) {
        int c = tourCost();
        if (cost > c) {
            cost = c;
            for (int i = 0; i < numCities; i++) tempTour[i] = tour[i];
        }
    } else {
        for (int i = start; i <= end; i++) {
            swap(&array[start], &array[i]);
            permute(array, start + 1, end);
            swap(&array[start], &array[i]);
        }
    }
}

void exhaustiveSearch() {
    cost = INT_MAX;
    lenTour = numCities;
    for (int i = 0; i < numCities; i++) tour[i] = i;
    permute(tour, 0, numCities - 1);
    for (int i = 0; i < numCities; i++) tour[i] = tempTour[i];
}
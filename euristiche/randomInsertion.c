/*
Nearest Insertion è una euristica costruttiva per il problema del TSP
*/

//#include "graphGenerator.c"


void randomInsertion() {
    // inizializzo seed per i numeri casuali
    struct timespec ts;
    if (clock_gettime(CLOCK_REALTIME, &ts) == -1) {
        perror("clock_gettime");
        return;
    }
    unsigned int seed = ts.tv_nsec;
    srand(seed);

    cost = 0;
    // inizializzo tutti i vertici come non visitati
    for (int i = 0; i < numCities; i++) visited[i] == 0;
    // inizializzo il subtour con la coppia di vertici con costo minore
    int minDistance = INT_MAX;
    for (int i = 0; i < numCities; i++) {
        for (int j = 0; j < i; j++) {
            if (adjacencyMatrix[i][j] < minDistance) {
                minDistance = adjacencyMatrix[i][j];
                tour[0] = i;
                tour[1] = j;
            }
        }
    }
    visited[tour[0]] = 1;
    visited[tour[1]] = 1;
    lenTour = 2;

    int r;
    while(lenTour < numCities) {
        // scelgo casualmente il nodo da inserire
        int r = rand() % numCities;
        while (visited[r]) {
            r = rand() % numCities;
        }
        // scelgo casualmente l'arco in cui inserire r
        int i = tour[rand() % (lenTour - 1)];
        int j = tour[i + 1];
        insertNode(r, i, j);
        visited[r] = 1;
    }
    // aggiungo l'ultima città non visitata
    for (int r = 0; r < numCities; r++) {
        if (!visited[r]) {
            tour[numCities - 1] = r;
            break;
        }
    }
    cost = tourCost();
}
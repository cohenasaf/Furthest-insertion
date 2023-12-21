#include "graphGenerator.c"
#include "nearestInsertion.c"
#include "nearestNeighbor.c"
#include "exhaustiveSearch.c"

int main() {
    generaNMatriciCasuali(5, 5);
    readRandomGraphFileInt(0);
    
    printf("\n");
    printMatrix();
    printf("\n");
    
    testEuristicCost(numCities, nearestNeighbor);
    printf("costo neighbor %d\n", cost);
    printTour();
    testEuristicCost(numCities, nearestInsertion);
    printf("costo nearest %d\n", cost);
    printTour();
    testEuristicCost(numCities, exhaustiveSearch);
    printf("costo exhaustive %d\n", cost);
    printTour();
}
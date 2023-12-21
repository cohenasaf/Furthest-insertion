#include "graphGenerator.c"
#include "nearestInsertion.c"
#include "nearestNeighbor.c"

int main() {
    //generaNMatriciCasuali(5, 20);
    readRandomGraphFileInt(1);
    
    printf("\n");
    printMatrix();
    printf("\n");
    
    testEuristicCost(numCities, nearestNeighbor);
    printf("costo neighbor %d\n", cost);
    printTour();
    testEuristicCost(numCities, nearestInsertion);
    printf("costo nearest %d\n", cost);
    printTour();
}
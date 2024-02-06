#include "graphGenerator.c"
#include "nearestInsertion.c"
#include "nearestNeighbor.c"
#include "cheapestInsertion.c"
#include "exhaustiveSearch.c"

int main() {
    generaNMatriciCasuali(5, 50);
    readRandomGraphFileInt(0);
    
    //printMatrix();
    
    testEuristicCost(numCities, nearestNeighbor);
    printf("costo neighbor %d\n", cost);
    printTour();
    testEuristicCost(numCities, nearestInsertion);
    printf("costo nearest %d\n", cost);
    printTour();
    testEuristicCost(numCities, cheapestInsertion);
    printf("costo cheapest %d\n", cost);
    printTour();
}
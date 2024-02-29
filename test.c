#include "graphGenerator.c"
#include "euristiche/nearestInsertion.c"
#include "euristiche/nearestNeighbor.c"
#include "euristiche/cheapestInsertion.c"
#include "euristiche/exhaustiveSearch.c"
#include "euristiche/farthestInsertion.c"
#include "euristiche/furthestInsertion.c"
#include "euristiche/randomInsertion.c"

int main() {
    //generaNMatriciCasuali(5,10);
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
    testEuristicCost(numCities, farthestInsertion);
    printf("costo farthest %d\n", cost);
    printTour();
    testEuristicCost(numCities, furthestInsertion);
    printf("costo furthest %d\n", cost);
    printTour();
    testEuristicCost(numCities, randomInsertion);
    printf("costo random %d\n", cost);
    printTour();

    readOptTour("0.opt");
    printf("Optimal Tour is:\n");
    printTour();
    cost = tourCost();
    printf("costo ottimale %d\n", cost);
}
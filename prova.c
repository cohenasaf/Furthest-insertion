#include <time.h>
#include <stdio.h>
#include "euristicTest.h"

int main() {
    tour[0] = 0;
    tour[1] = 1;
    lenTour = 2;
    printTour();
    insertNode(100, 1, 0);
    printTour();
}
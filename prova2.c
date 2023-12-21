#include <time.h>
#include <stdio.h>
#include <unistd.h> // notice this! you need it!

int main() {
    while(1) {
        clock_t c = clock();
        printf("%ld\n", clock() - c);
        sleep(1);
    }
}
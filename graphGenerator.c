#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE* file_ptr = fopen("grafi casuali/FILE_NAME", "w");
    fprintf(file_ptr, "testo");
    fclose(file_ptr);
    return 0;
}
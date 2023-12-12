#include "linkedList.h"

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

int main() {
    struct node *n = createNode(0);
    for (int i = 2; i < 10; i++) {
        add(n, i);
    }
    printLinkedList(n);
    insertNodeByPosition(n, 100, 3);
    insertNodeByValue(n, 23, 5);
    insertNodeByValue(n, 232, 5);
    insertNodeByValue(n, 2132, 5);
    printLinkedList(n);
    printf("%d\n", getValueByIndex(n, 5));
    printf("%s\n", contains(n, 9) ? "True" : "False");
}
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct node
{
  int data;
  struct node *next;
};

struct node *createNode(int value) {
    struct node *n = malloc(sizeof(struct node));
    n -> data = value;
    n -> next = NULL;
    return n;
}

// aggiunge il nodo "value" alla fine della lista
struct node *add(struct node *n, int value) {
    while(n -> next != NULL) n = n -> next;
    struct node *m = malloc(sizeof(struct node));
    m -> data = value;
    m -> next = NULL;
    n -> next = m;
    return n;
}

// inserisce un nuovo nodo tra il nodo
// in posizione "position" e il successivo,
// restituisce 0 se l'inserimento avviene correttamente
// -1 altrimenti
int insertNodeByPosition(struct node *n, int value, int position) {
    for (int i = 0; i < position; i++) {
        if (n == NULL) return -1;
        n = n -> next;
    }
    struct node *succ = n -> next;
    struct node *new = createNode(value);

    n -> next = new;
    new -> next = succ;
    return 0;
}

// inserisce un nuovo nodo v1 tra il nodo v2 e il successivo,
// restituisce 0 se l'inserimento avviene correttamente
// -1 altrimenti
int insertNodeByValue(struct node *n, int v1, int v2) {
    while (n -> data != v2) {
        if (n == NULL) return -1;
        n = n -> next;
    }
    struct node *succ = n -> next;
    struct node *new = createNode(v1);

    n -> next = new;
    new -> next = succ;
    return 0;
}

// Crea un nodo e lo inserisce come next di n
struct node *createLink(struct node *n, int value) {
    struct node *m = malloc(sizeof(struct node));
    m -> data = value;
    m -> next = NULL;
    n -> next = m;
    return n;
}

// restituisce true se la lista contiene il valore, false altrimenti
int contains(struct node *n, int value) {
    while(n != NULL) {
        if (n -> data == value) return true;
        n = n -> next;
    }
    return false;
}

int getValueByIndex(struct node *n, int idx) {
    int count = 0;
    while(count < idx) {
        n = n -> next;
        count++;
    }
    return n -> data;
}

int printLinkedList(struct node *n) {
    printf("[");
    do {
        printf("%d", n -> data);
        n = n -> next;
        if (n != NULL) printf(" - ");
    } while(n != NULL);
    printf("]\n");
    return 0;
}
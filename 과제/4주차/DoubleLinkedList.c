#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "DoubleLinkedList.h"

linkedList_h* createLinkedList_h(void) {
    linkedList_h* DL = (linkedList_h*)malloc(sizeof(linkedList_h));

    if (DL == NULL) {
        printf("malloc ½ÇÆÐ\n");
        exit(1);
    }

    memset(DL, 0, sizeof(linkedList_h));  
    return DL;
}

void printList(linkedList_h* DL) {
    listNode* p;
    printf("DL = (");
    p = DL->head;

    while (p != NULL) {
        printf("%s", p->data);
        p = p->rlink;
        if (p != NULL) printf(", ");
    }
    printf(")\n");
}

void insertNode(linkedList_h* DL, listNode* pre, char* x) {
    listNode* newNode;
    newNode = (listNode*)malloc(sizeof(listNode));
    strcpy(newNode->data, x);

    if (DL->head == NULL) {
        newNode->rlink = NULL;
        newNode->llink = NULL;
        DL->head = newNode;
    }
    else {
        newNode->rlink = pre->rlink;
        pre->rlink = newNode;
        newNode->llink = pre;
        if (newNode->rlink != NULL)
            newNode->rlink->llink = newNode;
    }
}

void deleteNode(linkedList_h* DL, listNode* old) {
    if (DL->head == NULL) return;
    else if (old == NULL) return;
    else {
        if (old->llink != NULL)
            old->llink->rlink = old->rlink;
        else
            DL->head = old->rlink;

        if (old->rlink != NULL)
            old->rlink->llink = old->llink;

        free(old);
    }
}

listNode* searchNode(linkedList_h* DL, char* x) {
    listNode* temp;
    temp = DL->head;

    while (temp != NULL) {
        if (strcmp(temp->data, x) == 0) return temp;
        else temp = temp->rlink;
    }
    return temp;
}

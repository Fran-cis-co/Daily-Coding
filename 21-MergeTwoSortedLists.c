/*
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* Create node struct and do typedef that way we only have to reference the struct with the word "Node" */
typedef struct Node{
    int data;
    struct Node* next;
} Node;

/* Method to push a new node into the front of the linked list */
void push(Node** head, int data)
{
    /* Allocate Node*/
    Node* new_node = (Node*)malloc(sizeof(Node));

    /* Put data in new node*/
    new_node->data = data;

    /* Insert node in front of list by having pointer point to the head node */
    new_node->next = (*head);

    /* Have the new head node reference the newly inserted node */
    (*head) = new_node;
}

/* Method to append node at the end of the list*/
void append(Node** head, int data)
{
    Node* new_node = (Node*)malloc(sizeof(Node));

    Node* last = *head;

    new_node->data = data;
    new_node->next = NULL;

    if(last == NULL)
    {
        *head = new_node;
        return;
    }

    while(last->next != NULL)
    {
        last = last->next;
    }

    last->next = new_node;
    return;
}

/* Method to print out a list */
void printList(Node* head)
{
    /* While the head is not null, print whatever data is inside */
    while (head)
    {
        printf("%i ", head->data);
        head = head->next;
    }
    /* Print double breaks to seperate between multiple prints of lists */
    printf("\n\n");
}

/* Method to merge the two lists */
void mergeLists(Node* list1, Node* list2)
{
    /* Create new lists of all merged nodes from both lists */
    Node* list3 = NULL;

    /* Iterate through both lists to ensure we get every node */
    while(list1->next != NULL && list2->next != NULL)
    {
        int data1 = list1->data;
        int data2 = list2->data;

        if(data1 == data2)
        {
            append(&list3, data1);
            append(&list3, data1);
        }
        else if (data1 > data2)
        {
            append(&list3, data2);
            append(&list3, data1);
        }
        else if (data2 > data1)
        {
            append(&list3, data1);
            append(&list3, data2);
        }

        list1 = list1->next;
        list2 = list2->next;
    }

    printList(list3);
}


/* Driver Code */
int main()
{   
    /* Test cases to input into the linked list*/
    int list1Arr[3] = {1, 2, 4};
    int list2Arr[3] = {1, 3, 4};

    /* Create Lists and input data */
    Node* list1 = malloc(sizeof(Node));
    list1->next = NULL;
    Node* list2 = malloc(sizeof(Node));
    list2->next = NULL;
    
    for(int i = (sizeof(list1Arr) / sizeof(int)) - 1; i >= 0; i--)
    {
        push(&list1, list1Arr[i]);
        push(&list2, list2Arr[i]);
    }

    /* Call method to merge lists */
    mergeLists(list1, list2);

    /* Free up allocated space */
    free(list1);
    free(list2);
    return 0;
}

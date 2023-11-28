#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 * Author: Tolulope Fakunle
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new = malloc(sizeof(listint_t)), *current = *head;

    if (!new)
        return NULL;

    new->n = number;

    if (!current || current->n >= number)
    {
        new->next = current;
        *head = new;
        return new;
    }

    while (current->next && current->next->n < number)
        current = current->next;

    new->next = current->next;
    current->next = new;

    return new;
}
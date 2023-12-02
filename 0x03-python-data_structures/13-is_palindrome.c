#include "lists.h"

/**
 * reverse - reverses the second half of the list
 *
 * @h_r: head of the second half
 * Return: no return
 */
void reverse(listint_t **h_r)
{
    listint_t *prv = NULL, *crr = *h_r, *nxt;

    while (crr != NULL)
    {
        nxt = crr->next;
        crr->next = prv;
        prv = crr;
        crr = nxt;
    }

    *h_r = prv;
}

/**
 * compare - compares each int of the list
 *
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */
int compare(listint_t *h1, listint_t *h2)
{
    listint_t *tmp1 = h1, *tmp2 = h2;

    while (tmp1 != NULL && tmp2 != NULL)
    {
        if (tmp1->n != tmp2->n)
            return 0;

        tmp1 = tmp1->next;
        tmp2 = tmp2->next;
    }

    return tmp1 == NULL && tmp2 == NULL;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev_slow = *head, *scn_half, *middle = NULL;
    int isp = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        if (fast != NULL)
        {
            middle = slow;
            slow = slow->next;
        }

        scn_half = slow;
        prev_slow->next = NULL;
        reverse(&scn_half);
        isp = compare(*head, scn_half);

        if (middle != NULL)
        {
            prev_slow->next = middle;
            middle->next = scn_half;
        }
        else
        {
            prev_slow->next = scn_half;
        }
    }

    return isp;
}
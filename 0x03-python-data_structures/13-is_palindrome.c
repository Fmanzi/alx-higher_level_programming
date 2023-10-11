#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - fn checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
listint_t *mid = NULL;
listint_t *second_half = NULL;
int is_palindrome = 1;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev = slow;
slow = slow->next;
}

if (fast != NULL)
{
mid = slow;
slow = slow->next;
}

second_half = slow;
prev->next = NULL;
reverse_list(&second_half);

is_palindrome = compare_lists(*head, second_half);

reverse_list(&second_half);
if (mid != NULL)
{
prev->next = mid;
mid->next = second_half;
}
else
{
prev->next = second_half;
}

return (is_palindrome);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to a pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
}

/**
 * compare_lists - compares two linked lists for equality
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
listint_t *temp1 = head1;
listint_t *temp2 = head2;

while (temp1 != NULL && temp2 != NULL)
{
if (temp1->n != temp2->n)
return (0);
temp1 = temp1->next;
temp2 = temp2->next;
}
if (temp1 != NULL || temp2 != NULL)
return (0);

return (1);
}

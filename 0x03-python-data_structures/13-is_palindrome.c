#include "lists.h"

/**
 * is_palindrome - a function in C that checks if
 * a singly linked list is a palindrome.
 * @head: the first node in linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!*head)
		return (1);

	/*To get middle of the linked list using 2 pointer techniques*/
	listint_t *slow, *fast;

	slow = fast = *head;

	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/*head of the second half of the list*/
	listint_t *head_sec_half = NULL;
	listint_t *ptr = slow->next;

	while (ptr)
	{
		listint_t *next = ptr->next;

		ptr->next = head_sec_half;
		head_sec_half = ptr;
		ptr = next;
	}
	/*Compare the first half and the reversed second half*/
	listint_t *first = *head;
	listint_t *second = head_sec_half;

	while (second)
	{
		if (first->n != second->n)
			return (0);

		first = first->next;
		second = second->next;
	}
	return (1);
}

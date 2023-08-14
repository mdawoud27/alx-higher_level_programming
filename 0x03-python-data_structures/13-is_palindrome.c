#include "lists.h"

/**
 * is_palindrome - A function that checks if
 * a singly linked list is a palindrome.
 * @head: The first node in linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/*To get the middle of the list we use 2 pointers technique*/
	listint_t *slow, *fast;

	slow = fast = *head;

	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next;
	}

	/*Here i will make the second half list*/
	listint_t *head_sec_half = NULL, *ptr = slow->next;

	while (ptr)
	{
		listint_t *next = ptr->next;

		ptr->next = head_sec_half;
		head_sec_half = ptr;
		ptr = next;
	}

	/*Compare the first half and the reversed second half*/
	listint_t *first = *head, *second = head_sec_half;

	while (second)
	{
		if (first->n != second->n)
			return (0);

		first = first->next;
		second = second->next;
	}
	return (1);
}

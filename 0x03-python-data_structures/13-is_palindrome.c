#include "lists.h"

/**
 * is_palindrome - Check if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *rev_list = NULL, *next = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = rev_list;
		rev_list = slow;
		slow = next;
	}

	if (fast != NULL)
		slow = slow->next;

	while (rev_list != NULL && slow != NULL)
	{
		if (rev_list->n != slow->n)
			return (0);
		rev_list = rev_list->next;
		slow = slow->next;
	}

	return (1);
}

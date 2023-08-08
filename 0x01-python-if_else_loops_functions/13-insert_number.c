#include "lists.h"

/**
 * insert_node - function  that inserts a number into
 * a sorted singly linked list.
 * @head: linked list head
 * @number: new node data
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *ptr;

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	
	ptr = *head;

	while (ptr->next && ptr->next->n < number)
		ptr = ptr->next;

	new_node->next = ptr->next;
	ptr->next = new_node;

	return (new_node);
}

#include "lists.h"

/**
 * insert_node - insert number to sorted singly linked list
 * @head: head of the linked list
 * @number: inserted number
 * Return: 0 if fail else point to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_list = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node_list == NULL || node_list->n >= number)
	{
		new->next = node_list;
		*head - new;
		return (new);
	}

	while (node_list && node_list->next && node_list->next->n
			< number)
		node_list = node_list->next;
	new->next = node_list->next;
	node->next = new;

	return (new);
}

#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - reverse linked list
 * @head: pointer to the frist node of reverse list
 * Return: pointer to the first node of new reverse list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node_l = *head, *next, *prev_l = NULL;

	while (node_l)
	{
		next = node_l->next;
		node_l->next = prev_l;
		prev_l = node_l;
		node_l = next;
	}

	*head = prev_l;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the linked list
 *
 * Return: 0 if not palindrome, else 1 if is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp_1, *reverse_1, *midd_1;
	size_t size_1 = 0, a;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp_1 = *head;
	while (temp_1)
	{
		size_1++;
		temp_1 = temp_1->next;
	}

	temp_1 = *head;
	for (a = 0; a < (size_1 / 2) - 1; a++)
		temp_1 = temp_1->next;

	if ((size_1 % 2) == 0 && temp_1->n != temp_1->next->n)
		return (0);

	temp_1 = temp_1->next->next;
	reverse_1 = reverse_listint(&temp_1);
	midd_1 = reverse_1;

	temp_1 = *head;
	while (reverse_1)
	{
		if (temp_1->n != reverse_1->n)
			return (0);
		temp_1 = temp_1->next;
		reverse_1 = reverse_1->next;
	}
	reverse_listint(&midd_1);

	return (1);
}

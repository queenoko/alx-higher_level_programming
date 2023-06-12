#include "lists.h"

/**
 * reverse_listint - reverse linked list
 * @head: pointer to the frist node of list
 * Return: pointer to the first node of new list
 */
void reverse_listint(listint **head)
{
	listint_t *former = NULL;
	listint_t *present = *head;
	listint_t *next = NULL;

	while (present)
	{
		next = present->next;
		present->next = former;
		former = present;
		present = next;
	}

	*head = former;
}

/**
 * is_palindrome - checks if linked is palindrome
 * @head: double pointer to linked list
 *
 * Return: 1 if true, else 0 if false
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_l = *head, *fast_l = *head, *temp_l = *head, *duplic = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast_l = fast_l->next->next;
		if (!fast_l)
		{
			duplic = slow_l->next;
			break;
		}
		if (!fast_l->next)
		{
			duplic = slow_l->next->next;
			break;
		}
		slow_l = slow_l->next;
	}

	reverse_listint(&duplic);

	while (duplic && temp_l)
	{
		if (temp_l->n == duplic->n)
		{
			duplic = duplic->next;
			temp_l = temp_l->next;
		}
		else
			return (0);
	}

	if (!duplic)
		return (1);

	return (0);
}

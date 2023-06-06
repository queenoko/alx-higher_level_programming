#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all listint_t list
 * @h: points to the head of a list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *pres;
	unsigned int x;
	
	pres = h; /* no of nodes */
	x = 0;
	while (pres != NULL)
	{
		printf("%i\n", pres->x);
		pres = pres->next;
		x++;
	}
	return (x);
}

/**
 * add_nodeint - adds new node at the top of listint_t list
 * @head: pointer to the top of the list
 * @n: include integer to node
 * Return: address of new element else NULL if fail
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *fresh;

	fresh = malloc(sizeof(listint_t));
	if (fresh == NULL)
		return (NULL);
	fresh->n = n;
	fresh->next = *head;
	*head = fresh;
	return (fresh);
}

/**
 * free_listint - frees a list
 * @head: pointer to a free list
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *pres;

	while (head != NULL)
	{
		pres = head;
		head = head->next;
		free(pres);
	}
}

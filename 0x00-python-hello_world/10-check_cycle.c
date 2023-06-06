#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if linked list contains cycle
 * @list: singly linked list
 * Return: 0 if no cycle, else 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *hd, *tal;

	if (list == NULL || list->next == NULL)
		return (0);

	hd = list->next;
	tal = list->next->next;

	while (hd && tal && tal->next)
	{
		if (hd == tal)
			return (1);

		hd = hd->next;
		tal = tal->next->next;
	}

	return (0);
}

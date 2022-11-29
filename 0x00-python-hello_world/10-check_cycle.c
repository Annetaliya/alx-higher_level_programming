#include "lists.h"

/**
 *check_cycle - function that detects a loop cycle in list
 *@list: pointer to head node
 *
 *Return: 1 if there is a cycle else 0 if there is none
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_p = list, *fast_p = list;

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;

		if (slow_p == fast_p)
		{
			return (1);
		}
	}
	return (0);
}


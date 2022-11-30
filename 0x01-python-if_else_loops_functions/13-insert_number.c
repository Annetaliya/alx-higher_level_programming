#include "lists.h"
#include <stdlib.h>

/**
 *insert_node - function that inserts a node to
 *a sorted linked list
 *@head: points to the head node
 *@number: the new node to be inserted
 *Return: Address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	new_node->next = NULL;


	if (*head == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		while (temp->next != NULL && temp->next->n < new_node->n)
		{
			temp = temp->next;
		}
		new_node->next = temp->next;
		temp->next = new_node;
	}
	return (new_node);
}

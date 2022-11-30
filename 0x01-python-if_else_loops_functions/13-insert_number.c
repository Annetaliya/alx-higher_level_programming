#include "lists.h"

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

	new_node = malloc(sizeof(listin_t));
	new_node->n = number;
	new_node->next = NULL;

	int key = number;

	if (head == NULL || key < *head->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		while (temp->next != NULL && temp->next->n < key)
			temp = temp->next;
		new_node->next = temp->next;
		temp->next = new_node;
	}
	return (new_node);
}

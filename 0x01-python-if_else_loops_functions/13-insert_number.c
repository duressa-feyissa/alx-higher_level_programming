#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

/**
 * insert_node - A function inserts a number into a sorted singly linked list.
 * @head: Pointer to head of list
 * @number: Value add to new node
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current, *hold;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	if (number < current->n) /*Check if we have to add */
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current->next != NULL)
	{
		current = current->next;
	}

	if (current->next == NULL && current->n < number)
	{
		current->next = new;
		return (new);
	}

	current = *head;
	while (current->n < number)
	{
		hold = current;
		current = current->next;
	}
	hold->next = new;
	new->next = current;

	return (new);
}

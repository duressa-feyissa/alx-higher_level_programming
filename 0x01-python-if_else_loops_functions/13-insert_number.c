#include <stdlib.h>
#include "lists.h"

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

	if (*head == NULL || head == NULL)
		return (NULL)
	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		free(new)
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	while (current->n < number)
	{
		hold = current;
		current = current->next;
	}
	hold->next = new;
	new->next = current;

	return (new);
}

#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: pointer to head of list
 * Return:  0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int *hold, count, i, j, check;
	listint_t *current;

	current = *head;
	if (current == NULL || current->next == NULL)
		return (1);
	if (current->next->next == NULL)
		return (1);
	count = 0;
	while (current)
	{
		current = current->next;
		count++;
	}
	hold = malloc(sizeof(int) * count);
	if (hold == NULL)
		return (0);
	current = *head;
	i = 0;
	while (current)
	{
		hold[i] = current->n;
		current = current->next;
		i++;
	}
	i = 0,	j = count - 1, check = 0;
	while (i < count)
	{
		if (hold[i] == hold[j])
			check++;
		i++;
		j--;
	}
	free(hold);
	if (check == count)
		return (1);
	return (0);
}

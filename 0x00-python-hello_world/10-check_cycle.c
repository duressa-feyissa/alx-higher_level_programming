#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: pointer to a pointer of the start of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	fast = (void *)list;
	slow = (void *)list;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);

	if (list->next->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;
	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

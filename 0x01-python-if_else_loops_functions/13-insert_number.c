#include "lists.h"

/**
 * insert_node - inserts a node in linked list
 * @head: pointer to head
 * @number: integer to add to node
 * Return: address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *arrlist, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!*head)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	
        arrlist	= *head;
	if (number <= arrlist->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (number >= arrlist->next->n && arrlist->next)
	{
		arrlist = arrlist->next;
		if (arrlist->next == NULL && number < arrlist->n)
		{
			new_node = add_nodeint_end(head, number);
			if (!new_node)
				return (NULL);
			return (new_node);
		}
	}
	new_node->next = arrlist->next;
	arrlist->next = new_node;
	return (new_node);
}

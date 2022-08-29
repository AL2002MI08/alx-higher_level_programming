#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - palindrome of singly linked list
 * @head: pointer to pointer to the first node of listint_t list
 *
 * Return: return 1 if it's palindrome otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	unsigned int len = 0, i = 0, flag = 1, lastidx, *buf;

	current = *head;
	if (*head == NULL || head == NULL)
		return (1);

	while (current != NULL)
	{
		current = current->next;
		len++;
	}

	buf = malloc(sizeof(int) * len);
	if (buf == NULL)
		return (1);

	current = *head;
	while (current != NULL)
	{
		buf[i] = current->n;
		i++;
		current = current->next;
	}

	lastidx = len - 1;
	for (i = 0; i < len / 2; i++)
	{
		if (buf[i] != buf[lastidx - i])
		{
			flag = 0;
			break;
		}
	}
	free(buf);
	return (flag);
}

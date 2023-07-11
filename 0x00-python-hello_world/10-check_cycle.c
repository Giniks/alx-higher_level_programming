#include <lists.h>

typedef struct ListNode {
	int value;
	struct ListNode* next;
} listint_t;

/**
 * check_cycle - chrcks if a singke linked list has a cycle
 * @list: pointer to the begining of the nodelist
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t* ls = list;
	listint_t* hs = list;

	while (hs != NULL && hs->next != NULL)
	{
		ls = ls->next;
		hs = hs->next->next;

	if(ls == hs)
	{
		return (1);
	}
	}
	return (0);
}
int main()
{
	listint_t* node1 = malloc(sizeof(listint_t));
	listint_t* node2 = malloc(sizeof(listint_t));
	listint_t* node3 = malloc(sizeof(listint_t));
	listint_t* node4 = malloc(sizeof(listint_t));


	node1->value = 1;
	node2->value = 2;
	node3->value = 3;
	node4->value = 4;

	node1->next = node2;
	node2->next = node3;
	node3->next = node4;
	node4->next = node2;

	int result = check_cycle(node1);
	printf("cycle detection: %d\n", result);

	free(node1);
	free(node2);
	free(node3);
	free(node4);

	return (0);
}

#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *lento = list;
	listint_t *rapido = list;

	if(!list)
	return (0);
	
	while(rapido->next->next)
	{
		rapido = rapido -> next -> next;
		lento = lento -> next;
		if(lento == rapido)
			return(1);
	}
	return(0);
}

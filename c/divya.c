
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
void Create();
void Count();
void Search();
void Insert_At_Begginning();
void Insert_At_Middle();
void Insert_At_End();
void Delete_At_Begginning();
void Delete_At_Middle();
void Delete_At_End();
void display();
 struct node
{
 int data; 
 struct node *next;
}*start=NULL;
 int  main()
{
int ch;
while(1)
	{
	printf("\n----MENU OPERATION----\n");
	printf("\n 1. Create ");
	printf("\n 2. Count");
	printf("\n 3. Search");
	printf("\n 4. Insert_At_Begginning ");
	printf("\n 5. Insert_At_Middle");
	printf("\n 6. Insert_At_End");
	printf("\n 7. Delete_At_Begginning");
	printf("\n 8. Delete_At_Middle ");
	printf("\n 9. Delete_At_Begginning");
	printf("\n 10.display");
	printf("\n 11.Exit");
	
	printf("\n\t Enter your choice:");
	scanf("%d",&ch);
	switch(ch)
{
		case 1: Create();
		        break;
		case 2: Count();
		        break;
		case 3:	Search();
		        break;
		case 4: Insert_At_Begg();
		        break;
		case 5: Insert_At_Middle();
		        break;
		case 6:	Insert_At_End();
		        break;
		case 7: Delete_At_Begg();
	         	break;
		case 8: Delete_At_Middle();
		        break;
		case 9: Delete_At_End();
		        break;
		case 10: display();
		        break;
		case 11: exit(0);
		default: printf("Invalid Choice:");			
}
}
return 0;
}

void Create()
{
	struct node *newnode,*current;
	int ch;
	do
{
newnode=(struct node *)malloc(sizeof(struct node));
	printf("Enter Data:");
	scanf("%d",&newnode->data);
	newnode->next=NULL;
	if(start==NULL)
{
	start = newnode;
	current = newnode;
}else
{
	current->next=newnode;
	current = newnode;
}
	printf("Do you want to continue [y/n]:");
	ch = getche();
}while(ch=='y' || ch=='Y');	
}

void Count()
{
	struct node *temp;
	int count = 0;
	temp=start;
	while(temp)
{
		count ++;
		temp = temp->next;
}
	printf("Total no of elements :%d",count);
}

void Search()
{
	struct node *temp;
	int search,flag=0;
	printf("Enter value to be searched ?");
	scanf("%d",&search);
	if(search==NULL)
	printf("Linked list does not exist");
	else
{
	temp=start;
	while(temp)
{
	if(temp->data==search)
{
	flag ++;
	break;
}
	temp=temp->next;
}
	if(flag==0)
	printf("Element not found");
	else
	printf("Element Found");
}
}

void Insert_At_Begg()
{
	struct node *newnode;
	newnode = (struct node*)malloc(sizeof(struct node));
	printf("Enter data:");
	scanf("%d",&newnode->data);
	newnode->next = NULL;
	if( start == NULL)
	start=newnode;
	else
{
		newnode->next=start;
		start=newnode;
}
}

void Insert_At_Middle()
{
	struct node *newnode,*temp,*temp1;
	int position,i;
	
	newnode=(struct node*)malloc(sizeof(struct node));
	printf("Enter Data:");
	scanf("%d",&newnode->data);
	newnode->next=NULL;
	printf("Enter position :");
	scanf("%d",&position);
	
	if(position<=0 || start==NULL)
{
		printf("Invalid position:");
		return;
}
	temp = start;
	if(position == 1)
{
		newnode->next = start;
		start = newnode;
		return;
}
	for(i=2;i<position;i++)
{
		temp = temp->next;
		if(temp==NULL)
		break;
}
	if(temp==NULL)
	printf("position out of range:");
	else
{
		temp1 = temp->next;
		temp->next = newnode;
		newnode->next = temp1; 
}
}

void Insert_At_End()
{
	struct node *newnode,*temp;
	newnode =(struct node*)malloc(sizeof(struct node));
	printf("Enter Data:");
	scanf("%d",&newnode->data);
	newnode->next = NULL;
	if(start == NULL)
	start = newnode;
	else
{
		temp = start;
		while(temp->next)
{
			temp = temp->next;
}
		temp->next=newnode;
}
}

void Delete_At_Begg()
{
	struct node *temp;
	if(start==NULL)
	printf("Linked list is not exist:");
	else
{
		temp=start;
		start = start->next;
		printf("\nDeleted value:%d",temp->data);
		free(temp);
}
}

void Delete_At_Middle()
{
	struct node *temp,*temp1;
	int position,i;
	printf("Enter position:");
	scanf("%d",&position);
	if(position<=0 || start==NULL)
{
	printf("Invalid Position:");
	return;
}
	if(position==1)
{
		temp=start;
		printf("\nDeleted value:%d",temp->data);
		start=start->next;
		free(temp);
		return;
}
	temp=start;
	for(i=2;i<position;i++)
{
		temp = temp->next;
		if(temp==NULL)
		break;
}
	if(temp==NULL)
	printf("Position out Range:");
	else
{
		temp1=temp->next;
		temp->next=temp1->next;
		printf("\nDeleted value :%d",temp1->data);
		free(temp1);
}
}

void Delete_At_End()
{
	struct node *temp,*temp1;
	if(start==NULL)
{
	printf("Linked list does not exist ");
	return;
}
	if(start->next==NULL)
{
	temp=start;
	printf("\nDeleted value:%d",temp->data);
	start=NULL;
	free(temp);
	return;
}
	temp=start;
	while(temp->next->next)
{
		temp=temp->next;
}
		temp1=temp->next;
		temp->next=NULL;
	
	 printf("\nDeleted value:%d",temp1->data);
	 free(temp1);
}

void display()
{
	struct node *temp;
	if(start==NULL)
	printf("Linked list is Empty:");
	else
{
		temp=start;
	while(temp)
{
		printf("\t %d",temp->data);
		temp = temp->next;
}
	printf("\tNULL");
}
}

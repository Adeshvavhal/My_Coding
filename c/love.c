#include<stdio.h>
#include <conio .h>
#include<dos.h>

void main()
{
	clrscr();
	int i;
	textcolor(RED);
	textbackground(WHITE);
	for(i=1; i<120; i++)
	{
		cprintf(" I Love You \0");
		delay(200);
	}
	
	getch();
}
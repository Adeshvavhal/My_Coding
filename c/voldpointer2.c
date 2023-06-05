#include <stdio.h>
     
int main()
 {
	 char ch='A';
	 int i=11;
	 float f=9.09;
	 double d=89.9078;
	 
	 char *cp=&ch;
	 int *ip=&i;
	 float *fp=&f;
	 double *dp=&d;
	 
	 
	 	void *vp =&ch;
		
	
	 
	 vp = &i;
	 printf("Data refer by vp : %d\n",*(int*)vp);
    printf("Data refer by vp :%c\n",*(char*)vp);
   
   
   return 0;

   
}
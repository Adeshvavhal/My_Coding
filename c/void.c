#include<stdio.h>
     
int main()

 {
char ch = 'A';
int i =11;
float f =9.09;
double d =89.9078;

char *cp = &ch;
int *ip = &i;
float *fp = &f;
double *dp= &d;

void *vp = &ch;
vp =&i;

printf("Value of ch : %c\n",ch);
printf("Adderss of ch : %p\n",&ch);
printf("Value of inside cp : %p\n", cp);
printf("Data refer by cp : %c\n",*cp);
printf("Size of ch : %ld\n",sizeof(ch));
printf("Size of cp : %ld\n",sizeof(cp));
printf("Size of cp : %ld\n",sizeof(cp));

   return 0;

   
}
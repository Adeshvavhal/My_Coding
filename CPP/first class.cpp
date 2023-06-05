

#include<iostream>
   using namespace std;

class Maths
{
	public:
	int iNo1;
	int iNo2;
	
	Maths()
{
	iNo1=A;
	iNo2=B;


}
	Maths(int A,int B)
{
	iNo1=A;
	iNo2=B;
}
	int Addition()
{
	return iNo1+iNo2;

}
	int substraction()
{

	return iNo1-iNo2;
}

};  

int main()
 { 
     
	Maths mobj1;
	Maths mobj2(11,10);

   return 0; 
   
}

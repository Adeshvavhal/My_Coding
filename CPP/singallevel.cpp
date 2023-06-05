#include<iostream>
   using namespace std;  
   
   class Base
   {
	   public:
	   int A,B ;
	   
	   Base()
	   {
		   cout<<"Inside Base constructor\n";
	   }
	   
	   ~Base()
	   {
		   cout<<"Inside Base destructor\n";
	   }
	   
	   void fun()
	   {
		   cout<<"Inside Base fun\n";
	   }
   };
   
   class Derived : public Base
   {
	   public:
	   int X,Y;
	   
	   Derived()
	   {
		   cout<<"Inside Derived constructor\n";
	   }
	   
	   ~Derived()
	   {
		   cout<<"Inside Derived destructor\n";
	   }
	   
	   void gun()
	   {
		   cout<<"Inside Derived gun\n";
	   }
   };
	   
		   
int main()
 { 
     Derived * ptr = NULL;
	 
	 ptr = new Derived;
	 

   return 0; 
   
}

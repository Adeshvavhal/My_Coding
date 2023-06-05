
class Base
{
      public int A,B;
      public Base(int No1,int No2)
      {
            this.A = No1;
            this.B = No2;
      }
      public void fun()
      {
            System.out.println("Inside Base fun");
            System.out.println("Value of a from fun method is :"+this.A);
      }
}
class Derived extends Base
{
      public int X,Y;
      public Derived(int i,int j,int k , int l)
      {
            super(k,l);
            this.X = No1;
            this.Y = No2;
      }
      public void gun()
      {
            System.out.println("value of A from gun method :"+super.A);
            super.fun();
      }
}
class SuperDemo
{
      public static void main(String arg[])
      {
            Derived dobj= new Derived(11,21,51,101);
      }
}
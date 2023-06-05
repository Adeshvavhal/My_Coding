
class StaticDemo
{     
      static
      {
            System.out.println("inside static of static class with cotanis main");
      }
      public StaticDemo()
      {
            System.out.println("inside construtor of staticDemo");
              
      }
      public static void main(String arr[])    
        {
            System.out.println("Insid main");
            System.out.println("Value of static No3 :"+Demo.No3);
            System.out.println("Value of static No4 :"+Demo.No4);
            Demo.gun();

            Demo obj1 = new Demo();
            Demo obj2 = new Demo();

            obj1.Fun();

      }
}

class Demo
{
      public int No1;
      public int No2;
      public static int No3;
      public static int No4;

     
      public Demo()
      {
            System.out.println("Insid Comnstructor");
            No1 = 11;
            No2 = 21;
      }
       static
      {
            System.out.println("Insid static block");
            No3 = 51;
            No4 = 101;
            
      }
      public void Fun()
      {
              System.out.println("Insid Fun");
              System.out.println("value of No1 :"+this.No1);
              System.out.println("value of No2 :"+this.No2);
              System.out.println("value of No3 :"+this.No3);
              System.out.println("value of No4 :"+this.No4);
      }
      public static void gun()
      {
              System.out.println("Insid static method gun");
             // System.out.println("value of No1 :"+No1);
              //System.out.println("value of No2 :"+No2);
              System.out.println("value of No3 :"+No3);
              System.out.println("value of No4 :"+No4);
      }

      
}

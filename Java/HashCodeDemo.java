class Demo
{
      public int No1;
      public int No2;

      public Demo(int a, int b)
      {
            No1 = a;
            No2 = b;

      }
}
class HashCodeDemo
{
      public static void main(String a[])
      {
            String s1 ="Hello";
            String s2 ="Hello";

            System.out.println("Hascode of s1 :"+s1.hashCode());
            System.out.println("Hascode of s2 :"+s2.hashCode());
            if(s1.equals(s2))
            {
                  System.out.println("Object are same");
            }
            else
            {
                  System.out.println("Object are Different");

            }
            if(s1==s2)
            {
                  System.out.println("Object are same");
            }
            else
            {
                  System.out.println("Object are Different");

            }
      }
}
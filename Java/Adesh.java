import java.util.*;

class Adesh
{
      public static void main(String arg[])
      {
            Scanner sobj =  new Scanner(System.in);
            int iNo1 = 0;
            int iNo2 = 0;
            int iAns = 0;
          //  System.out.println("Entre first number:");
            iNo1 = sobj.nextInt();

           // System.out.println("Entre second number:");
            iNo2 = sobj.nextInt();

            iAns = iNo1 + iNo2;
            System.out.println("Addition is :"+iAns);
      }
}
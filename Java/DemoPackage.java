import java.util.*;

import Marvellous.Arithmatic;

import Marvellous.PPA;

class DemoPackage
{
      public static void main(String agr[])
      {
            Scanner sobj = new Scanner(System.in);

            System.out.println("Entre first number");
              int iNo1 = sobj.nextInt();

            System.out.println("Entre second number");
              int iNo2 = sobj.nextInt();

            Arithmatic aobj= new Arithmatic(iNo1,iNo2);

            int iResult = aobj.Addition();
            System.out.println("Addition is :"+iResult);

             iResult = aobj.Substraction();
             System.out.println("Substraction is :"+iResult);

             Loop lobj = new Loop();
            lobj.Display();

      }
}
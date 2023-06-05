
abstract class Arithmatic 
{
      public int Addition(int No1,int No2)
      {
            return No1 + No1;
      }
      public abstract int Substracction(int No1,int No2);
}
class Marvellous extends Arithmatic
{
      public  int Substracction(int No1,int No2)
      {
            return No1- No2;
      }
    
}
class AbstractDemo
{
      public static void main(String arg[])
      {
            Marvellous mobj = new Marvellous();
            int Ret = 0;
            Ret = mobj.Addition(11,11);
            System.out.println("Addition is :"+Ret);
            Ret = mobj.Substracction(11,10);
            System.out.println("Substraction is :"+Ret);

      }
}
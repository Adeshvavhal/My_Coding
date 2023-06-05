

 
class Loops
{
      public static void main(String arr[])
      {
            int Arr[] = {10,20,30,40};
            int iCnt = 0;

            System.out.println("Traversal of array using for loop");
            for(iCnt = 0; iCnt <Arr.length; iCnt++)
            {
                  System.out.println(Arr[iCnt]);
            }
             System.out.println("Traversal of array using for while loop");
            iCnt =0;
            while(iCnt < Arr.length)
            {
                  System.out.println(Arr[iCnt]);
                  iCnt++;
            }
            System.out.println("Traversal of array using for do while loop");
            iCnt =0;
            do
            {
                  System.out.println(Arr[iCnt]);
                  iCnt++;
            } while(iCnt < Arr.length);
             System.out.println("Traversal of array using for-each loop");
             for(int iNo:Arr)
             {
                  System.out.println(iNo);
             }
      }
}
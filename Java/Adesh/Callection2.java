import java.util.*;

class Callection2
{
      public static void main(String arg[])
      {
            LinkedList <String>lobj = new LinkedList<String>();

            lobj.add("kapil");
            lobj.add("Aditya");
            lobj.add("Rohan");
            lobj.add("Rutik");
            lobj.add("Tejas");
            
            System.out.println("Element of linked list are :"+lobj);

            lobj.addFirst("Pooja");
            System.out.println("Element of linked list are :"+lobj);

            lobj.addLast("Seha");
            System.out.println("Element of linked list are :"+lobj);

            Iterator iobj = lobj.iterator();
            System.out.println("Data using iterator:");
            while(iobj.hasNext())

            {
                  System.out.println(iobj.next());
            }
            if(lobj.contains("Rohan"))
            {
                  System.out.println("rohan is present in LL");
            }
            else
            {
                   System.out.println("Rohan is absent in LL");

            }

            lobj.remove();
            System.out.println("Element of linked list are :"+lobj);

            lobj.remove();
            System.out.println("Element of linked list are :"+lobj);

            lobj.remove(1);
            System.out.println("Element of linked list are :"+lobj);

            lobj.remove(0);
            System.out.println("Element of linked list are :"+lobj);

            lobj.removeLast();
            System.out.println("Element of linked list are :"+lobj);

            System.out.println("Number of element are :"+lobj.size());

            lobj.set(1,"Dipak");
            System.out.println("Element of linked list are :"+lobj);


                            

            lobj.clear();
            System.out.println("Element of linked list are :"+lobj);













      }
}
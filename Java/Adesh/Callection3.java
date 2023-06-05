import java.util.*;

class Book 
{
      public String Name;
      public int Price;

      public Book(String s,int i)
      {
            this.Name =s;
            this.Price =1;

      }
      public void Display()
      {
            System.out.println("Book name:" +this.Name+ "Price"+this.Price);
      }
}


class Collection3
{
      public static void main(String agr[])
      {
            LinkedList <Book> lobj =new LinkedList<Book>();

            lobj.add(new Book("Lets us C",400));
            lobj.add(new Book("Data Structure",500));
            lobj.add(new Book("C++ programing",980));
            lobj.add(new Book("Langular web development",700));

            Iterator iobj = lobj.iterator();
            Book bref=null;
            System.out.println("Element of linked list are:");
            while(iobj.hasNext())
            {
                  bref = (Book)iobj.next();
                  bref.Display();
            }

            lobj.clear();
      }

}
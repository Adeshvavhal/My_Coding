import java.util.*;
class Data 
{
  public Arr[]
  public Data(int size)
  {
    Arr = new int[size];

  }
  public void Accept()
  {
    Scanner sobj = new Scanner(System.in);
    System.out.println("Entre number");
    for(int i = o;i<Arr.lenght;i++)
    {
      Arr[i] = sobj.nextInt();
    }

  }
}
class DemoEven extends Thread
{
  public Data dobj;
  public DemoEven(Data obj)
  {
    dobj = obj;

  }
  public void run()
  {
    for(int i = 0; i<dobj.Arr.lenght;i++)
    {
      if(dobj.Arr[i]% 2 ==0)
      {
        System.out.println("Even Number is :"+dobj.Arr[i]);
      }
    }
  }
}
class DemoOdd extends Thread
{
  public Data dobj;
  public DemoOdd(Data obj)
  {
    dobj = obj;

  }
  public void run()
  {
    for(int i = 0; i<dobj.Arr.lenght;i++)
    {
      if(dobj.Arr[i]% !2 ==0)
      {
        System.out.println("odd Number is :"+dobj.Arr[i]);
      }
    }
  }
}
class ThrowsDemo5
{
  public static void main(String a[])
  {
    Data obj1 = new Demo(10);
    obj1.Accept();

    DemoEven eobj = new DemoEven(obj1);
    DemoOdd oobj = new DemoOdd(obj1);

    Thread t1 = new Thread(eobj);
    Thread t2 = new Thread(oobj);

    t1.start();
    t2.start();

    t1.join();
    t2.join();


  }
}
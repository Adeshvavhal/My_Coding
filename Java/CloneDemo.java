class Employe implements Cloneable
{
      public int Eid;
      public String Name;
      public int Salary;

      public Employe(int No, String str, int Value)
      {
            this.Eid = No;
            this.Name =str;
            this.Salary = Value;
      }
      public Object clone()throws CloneNotSupportedException
      {
            return super.clone();
      }

}


class CloneDemo
{
      public static void main(String a[])
      {
            try
            {
                  Employe eobj1 = new Employe(101,"Rahul",11000);
                  Employe eobj2 =(Employe)eobj1.clone();

                  System.out.println("Name of first employ :"+eobj1.Name);
                  System.out.println("Name of Second employ :"+eobj2.Name);

                  System.out.println("salary of 1 employ :"+eobj1.Salary);
                  System.out.println("salary of 2 employ :"+eobj2.Salary);
            
                  eobj1.Name ="Sagar";
                  System.out.println("Name of first employ :"+eobj1.Name);
                  System.out.println("Name of first employ :"+eobj2.Name);
                 
            }
            catch(CloneNotSupportedException obj)
            {}

      }
}
import javax.swing.*;
import java.awt.event.*;

class Calculator extends WindowAdapter implements ActionListener
{
      public JFrame mainfrane;
      public JButton b1,b2,b3,b4;
      public JTextField t1,t2;
      public JLabel lobj;
      Integer No1,No2;
      public Calculator(int width,int height,String Title)
      {
            mainfrane = new JFrame(Title);
            mainfrane.setSize(width,height);

            mainfrane.addWindowListener(this);

            t1 = new JTextField();
            t2= new JTextField();

            t1.setBounds(70,100,70,30);
            t2.setBounds(220,100,70,30);

            mainfrane.add(t1);
            mainfrane.add(t2);

            b1 = new JButton("Add");
            b2 = new JButton("Sub");
            b3 = new JButton("Mult");
            b4 = new JButton("Div");

            b1.setBounds(1,280,80,40);
            b2.setBounds(90,280,80,40);
            b3.setBounds(180,280,80,40);
            b4.setBounds(270,280,80,40);

            mainfrane.add(b1);
            mainfrane.add(b2);
            mainfrane.add(b3);
            mainfrane.add(b4);

            lobj = new JLabel();
            lobj.setBounds(150,25,200,100);
            mainfrane.add(lobj);

            b1.addActionListener(this);
            b2.addActionListener(this);
            b3.addActionListener(this);
            b4.addActionListener(this);

            mainfrane.setLayout(null);
            mainfrane.setVisible(true);


      }
      public void windowClosing(WindowEvent obj)
      {
            System.exit(0);
      }
      public void actionPerformed(ActionEvent obj)
      {
            try 
            {
                  No1 = Integer.persetInt(t1.getText());
                  No2 = Integer.persetInt(t2.getText());

                  if(obj.getSource()==b1)
                  {
                        lobj.setText("Addition is :"+(No1+No2));
                  }
                  else if(obj.getSource()==b2)
                  {
                        lobj.setText("Addition is :"+(No1-No2));
                        
                        
                  }
                  else if(obj.getSource()==b3)
                  {
                        lobj.setText("Addition is :"+(No1*No2));
                        
                        
                  }
                  else if(obj.getSource()==b4)
                  {
                        lobj.setText("Addition is :"+(No1/No2));
                        
                        
                  }




            }
            catch(Exception eobj)
            {

            }
      }

}
class MarvellousCalculater
{
      public static void main(String arg[])
      {
         Calculator cobj = new Calculator(400,400,"Marvellous Calculator");
      }
}
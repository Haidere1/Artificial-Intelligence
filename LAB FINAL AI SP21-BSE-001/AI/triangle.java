
import java.util.*;
public class triangle
{
    public static void main(String[] args){
    Scanner sc= new Scanner(System.in);
    try{
    System.out.println("Enter The Two angles For the Triangle <180 must be an integer Value :");
    int a=sc.nextInt();
    int b=sc.nextInt();
    if(a+b<180){

    int r=180 - (a+b);
    System.out.println("The Third Angle is = "+r);

    if(a < 90 && b < 90 && r < 90)
    {
        System.out.println("The Triangle is an acute triangle ");
    }
    else if(a>90 || b>90 || r>90)
    {
        System.out.println("The Triangle is an obtuse triangle ");
    }
    else if((a==90 && b<90 && r<90)  || (b==90 && a<90 && r<90) || (r==90 && b<90 && a< 90)  )
    {
        System.out.println("The Triangle is a Right angle triangle ");
    }

    }
    
    else{
        System.out.println("ERROR : The sum of two angles of a triangle can not be greater than 180.");
    }
    sc.close();
}
    
    catch(Exception e)
    {
        System.out.println("Enter Correct DATA TYPE : Integer");
    }

}
}

// there should be a condition to check the type of triangle when all the three angles are equal//

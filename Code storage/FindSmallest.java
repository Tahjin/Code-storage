import java.util.Scanner;

public class FindSmallest{
    public static String Smallest(int x,int y){
        if(x<y){
            return "The smallest number is "+x;
        }
        else if(x>y){
            return "The smallest number is "+y; 
        }
        else{
            return "Not real! they are the same";
        }
    }
    public static void main(String[]args){
        Scanner input = new Scanner(System.in);
        System.out.print("Please give a int for x: ");
        int num1 = input.nextInt();
        System.out.print("Please give a int for y: ");
        int num2 = input.nextInt();
        System.out.println(Smallest(num1,num2));

        input.close();

    }
}
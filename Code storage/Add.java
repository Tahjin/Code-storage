import java.util.Scanner;

public class Add {
    public static void main(String[]args){
        Scanner scnr = new Scanner(System.in);
        String Name;
        int firstNum;
        int secondNum;


        System.out.println("Enter your name: ");
        Name = scnr.nextLine();        
        System.out.println("Enter a number: ");
        firstNum = scnr.nextInt();
        System.out.println("Enter a second number: ");
        secondNum = scnr.nextInt();
        System.out.println("Here is some cool facts " + Name);
        System.out.println(firstNum +" + "+secondNum+" = "+(firstNum+secondNum));
        System.out.println("Also on top of that did you know");
        System.out.println(firstNum +" / "+secondNum+" = "+((double)firstNum/secondNum));
        scnr.close();

    }
}

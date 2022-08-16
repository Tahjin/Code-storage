import java.util.Scanner;

public class Again {
    public static void main(String[]args){
        Scanner scnr = new Scanner(System.in);
        int num = 0;
        boolean yo = true;
        while(yo){
            System.out.println("please enter 1,2,3 or -1 to quit: ");
            num = scnr.nextInt();
            if(num==1){
                System.out.println("phrase 1");
            }
            else if(num==2){
                System.out.println("phrase 2");
            }
            else if(num==3){
                System.out.println("phrase 3");
            }
            else if(num==-1){
                System.out.println("Goodbye");
                yo = false; 
            }
            else{
                System.out.println("that wasn't an option, try again");
            }
        }
        scnr.close();
    }
}

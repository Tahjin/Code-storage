import java.util.Scanner;

public class Mario{
    public static void main(String[]args){
        Scanner input = new Scanner(System.in);
        boolean yesorno = true;
        int height;
        do{
            System.out.print("Enter a height from 1-8 or (-1 to quit): ");
            height = input.nextInt();
            if(height>0 && height<9){
                for(int block=1;block!=height+1;block++){
                    for(int dotnum=height-block;dotnum!=0;dotnum--){
                        System.out.print(" ");
                    }
                    for(int num = 0;num!=block;num++){

                        System.out.print("#");
                    }
                    System.out.println("");
                }
                
            }
            else if(height==-1){
                yesorno = false;
            }
        }
        while(yesorno);           
        input.close();
    }
}
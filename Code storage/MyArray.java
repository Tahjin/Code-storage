import java.util.Random;
import java.util.Scanner;

public class MyArray {
    public static void main(String[]args){
        Scanner input = new Scanner(System.in);
        int[] arr = new int[10];
        String[] arr2 = {"hello","turtle","talyn","lol"};
        double[] arr3 = {0.0,0.4,5.4,2.0,4.0};
        int i=0;
        while(i!=10){
            System.out.print("Input number: ");
            arr[i]=input.nextInt();
            ++i;
        }

        int sum=0;
        int lowest=100000000;
        for(int j=0;j<arr.length;++j){
            sum+=arr[j];
            if(arr[j]<lowest){
                lowest=arr[j];
            }
        }
        double avg = sum/10.0;
        System.out.println("Total: "+sum);
        System.out.println("Lowest: "+lowest);
        System.out.println("Average: "+avg);

        System.out.println("is talyn in array: "+find(arr2,"talyn"));
        System.out.println("the biggest number in array is: "+findMax(arr3));
        char[] charArr1 = convertToArray("talyn");
        for(int j=0;j<charArr1.length;++j){
            System.out.print(charArr1[j]+", ");
        }
        System.out.println("");      
        System.out.println(convertToString(charArr1));
        int[] arr4 =populateArray(4, 10);
        for(int j=0;j<arr4.length;++j){
            System.out.print(arr4[j]+", ");
        }
        input.close();
    }
    /**
     * checks if t in array s
     * @param s array of strings
     * @param t target it searches for
     * @return returns true if t in array s
     */
    public static boolean find(String[] s,String t){
        for(int j=0;j<s.length;++j){
            if(s[j]==t){
                return true;   
            }  
        }
        return false;
    }
    /**
     * looks for bigest number in array D
     * @param D array of double
     * @return the largest number in array D
     */
    public static double findMax(double[] D){
        double bigest=-100000000.0;
        for(int j=0;j<D.length;++j){
            if(D[j]>bigest){
                bigest=D[j];   
            }  
        }
        return bigest;        
    }
    /**
     * turns a string into a array of char
     * @param s the original string
     * @return a array of char 
     */
    public static char[] convertToArray(String s){
        char[] charArr = new char[s.length()];
        for(int j=0;j<s.length();++j){
            charArr[j]=s.charAt(j);
        }
        return charArr;
    }
    /**
     * turns a array of char into a string
     * @param c array of char
     * @return a string by adding up array
     */
    public static String convertToString(char[] c){
        String yes = "";
        for(int j=0;j<c.length;++j){
            yes+=c[j];
        }
        return yes;
    }
    /**
     * makes a array with random numbers from predetermined range and size
     * @param size how big the array is 
     * @param max maximun range of random numbers
     * @return array of random numbers
     */

    public static int[] populateArray(int size,int max){
        int[] newArr = new int[size];
        Random rand = new Random();
        for(int j=0;j<newArr.length;++j){
            newArr[j]=rand.nextInt(max);
        }
        return newArr;        
    }

}

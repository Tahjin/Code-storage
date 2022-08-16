public class FindNeg {
    public static void main(String[]args){
        int[] array1 = {2, 4, 6, -1, 10, -20, 16, -3, 8};
        int numOfNegs=0;
        for(int i=0;i<array1.length;++i){
            if(array1[i]<0){
                numOfNegs+=1;
            }  
        }
        System.out.println("");
        System.out.println("The number of negatives in the array is "+numOfNegs);
    }
}

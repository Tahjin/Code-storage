import java.io.*;
import java.util.*;
//import java.lang.Math;

public class GraphPoints {
    public static void main(String[]args)throws IOException{
        Scanner fileinput = new Scanner(new File("coordinates.txt"));
        PrintWriter pr = new PrintWriter(new File("Answers"));
        double x1=fileinput.nextDouble();
        double y1=fileinput.nextDouble();
        double x2=fileinput.nextDouble();
        double y2=fileinput.nextDouble();

        double distance = Math.sqrt(Math.pow(x2-x1,2)+Math.pow(y2-y1,2));
        double midpoint1 = (x2+x1)/2;
        double midpoint2 = (y2+y1)/2;

        pr.println("Point A ("+x1+","+ y1+")");
        pr.println("Point B ("+x2+","+ y2+")");        
        pr.println("distance beetween points "+distance);
        pr.println("midpoint is ("+midpoint1+","+ midpoint2+")");

        pr.close();

    }
}
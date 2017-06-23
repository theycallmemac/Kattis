import java.io.BufferedInputStream;
import java.util.Scanner;

public class Kattis {
    
    public static double getNorm(double x1, double x2, double y1, double y2, double p){
        
        return Math.pow(Math.pow(Math.abs(x1 - x2), p) + Math.pow(Math.abs(y1 - y2), p), 1.0 / p);
        
    }
    
    public static void main(String[] args) {

        Scanner in = new Scanner(new BufferedInputStream(System.in));
        String[] input = in.nextLine().split(" ");

        while (input.length == 5) {

            double xOne = Double.parseDouble(input[0]);
            double yOne = Double.parseDouble(input[1]);

            double xTwo = Double.parseDouble(input[2]);
            double yTwo = Double.parseDouble(input[3]);

            double p = Double.parseDouble(input[4]);

            double norm = getNorm(xOne,xTwo, yOne, yTwo, p);
            System.out.println(norm);
            input = in.nextLine().split(" ");

        }
    }
}

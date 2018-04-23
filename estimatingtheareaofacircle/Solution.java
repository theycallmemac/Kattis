
import java.util.Scanner;

public class Solution {

	public static double getArea(double r, double m, double c){
		double area;
		area = Math.PI * (r * r);

		return area;

	}

	public static double getEstimatedArea(double r, double m, double c){

		double estimatedArea;
		estimatedArea = 4 * (r * r) * (c / m);

		return estimatedArea;
	}

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        double r = in.nextDouble();
        double m = in.nextDouble();
        double c = in.nextInt();


        double area;
        double estimatedArea;
        while(r != 0 || m != 0 || c != 0){

        	area = getArea(r,m,c);
        	estimatedArea = getEstimatedArea(r,m,c);

            System.out.println(area + " "+ estimatedArea);

            r = in.nextDouble(); 
            m = in.nextDouble();
            c = in.nextInt();

		}

    }
}

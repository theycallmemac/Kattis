
import java.util.Scanner;
import java.text.DecimalFormat;

class Solution {


	public static double getEuclidianArea(int radius){
		double pi = Math.PI;
		double area = (pi) * (radius * radius); 
		return area;

	}

	public static double getTaxiCabArea(int radius){
		double pi = Math.PI;
		double area = 2 * Math.pow(radius, 2);
		return area;

	}

	public static void main(String [] args){

		Scanner in = new Scanner(System.in);
		int radius = in.nextInt();
		double euclidianArea = getEuclidianArea(radius);
		double taxiCabArea = getTaxiCabArea(radius);
		System.out.println(euclidianArea);
		System.out.println(taxiCabArea);
    
	}
  
}

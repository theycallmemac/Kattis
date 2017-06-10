
import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int radius = in.nextInt();
        int crust = in.nextInt();
        int coveredInCheese = radius - crust;
        double area = (radius * radius) * Math.PI;
        double cheeseArea = (coveredInCheese * coveredInCheese) * Math.PI;
        System.out.println(cheeseArea * 100.0 / area);

    }
}

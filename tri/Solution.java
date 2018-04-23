
import java.util.Scanner;

public class Solution {

	public static void findEquation(int a, int b, int c){

        if(a == b + c) {
            System.out.printf("%d=%d+%d", a, b, c);
            return;
        }

        if(a == b - c) {
            System.out.printf("%d=%d-%d", a, b, c);
            return;
        }

        if(a == b * c) {
            System.out.printf("%d=%d*%d", a, b, c);
            return;
        }

        if(a == b / c) {
            System.out.printf("%d=%d/%d", a, b, c);
            return;
        }
        
		    if(a + b == c) {
            System.out.printf("%d+%d=%d", a, b, c);
            return;
        }
        if(a - b == c) {
            System.out.printf("%d-%d=%d", a, b, c);
            return;
        }

        if(a * b == c) {
            System.out.printf("%d*%d=%d", a, b, c);
            return;
        }

        if(a / b == c) {
            System.out.printf("%d/%d=%d", a, b, c);
            return;
        }

	}
	
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        findEquation(a,b,c);

    }
}

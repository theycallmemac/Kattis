import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int p = in.nextInt();

        for(int i = 0; i < p; i++){

        	int k = in.nextInt();
            System.out.print(k + " ");

            int n = in.nextInt();
            System.out.print((n * (n + 1) / 2) + " ");
            System.out.print(n * n + " ");
            System.out.print(n * (n + 1));
            System.out.println();
            
        }
        
    }

}

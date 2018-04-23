import java.util.Scanner;

public class Solution {

     public static void main(String[] args){

        Scanner in = new Scanner(System.in);
        long n = in.nextInt();
        long p = in.nextInt();
        long q = in.nextInt();


        long sets = p + q + (n * 2);
        long changes = sets / n;

        if(changes % 2 == 0){
           System.out.println("paul");
        }
        else{
           System.out.println("opponent");
        }
   }
}

import java.util.Scanner;

public class Kattis {

    public static void main(String[] args)
    {
    
        Scanner in = new Scanner(System.in);
        int[] input = {in.nextInt(), in.nextInt()};
        String output = (input[0] > input[1]? ("Dr. Chaz needs " + (input[0] - input[1]) + " more pieces of chicken!") : ("Dr. Chaz will have " + (input[1] - input[0]) + " pieces of chicken left over!"));
        if(Math.abs(input[1] - input[0]) == 1)
            output = output.replace("pieces", "piece");
        System.out.println(output);
        
    }
}

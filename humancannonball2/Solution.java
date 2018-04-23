import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        final double acc = 9.81;
        int cases = Integer.parseInt(br.readLine());
        
        while (cases-- > 0) {
        
            String[] values = br.readLine().split(" ");
            double v = Double.parseDouble(values[0]);
            double degrees = Math.toRadians(Double.parseDouble(values[1]));
            double d = Double.parseDouble(values[2]);
            double lh = Double.parseDouble(values[3]) + 1;
            double uh = Double.parseDouble(values[4]) - 1;

            double time = d / (v * Math.cos(degrees));
            double y = v * time * Math.sin(degrees) - acc * (1.0 / 2.0) * Math.pow(time, 2);

            if (lh <= y && uh >= y) {
                System.out.println("Safe");
            } 
            else {
                System.out.println("Not Safe");
            }
        }
    }
}

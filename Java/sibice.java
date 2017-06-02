
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Kattis {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] string = br.readLine().split(" ");
        int matches = Integer.parseInt(string[0]);
        int width = Integer.parseInt(string[1]);
        int height = Integer.parseInt(string[2]);

        while (matches-- > 0) {
            int length = Integer.parseInt(br.readLine());
            double diag = Math.sqrt(Math.pow(height, 2) + Math.pow(width, 2));

            if (length <= diag) {
                System.out.println("DA");
            } else {
                System.out.println("NE");
            }
        }

    }

}

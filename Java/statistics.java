import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
public class Kattis {
    public static void getRange(String stats, int cases) {
        int mini = Integer.MAX_VALUE;
        int maxi = Integer.MIN_VALUE;

        String[] numbers = stats.split(" ");
        for (int i = 1; i < numbers.length; i++) {
             int num = Integer.parseInt(numbers[i]);
             if (num < mini) {
                mini = num;
             }
             if (num > maxi) {
                maxi = num;
            }
        }
        System.out.printf("Case %d: %d %d %d\n", cases, mini, maxi, maxi - mini);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String stats = br.readLine();
        int cases = 1;
        while (stats != null) {
            getRange(stats, cases);
            stats = br.readLine();
            cases++;
        }
    }
}

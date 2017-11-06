import java.util.Scanner;
public class Kattis {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int avg = n;
        int total = 0;
        for(int i = 0; i < n; i++){
            int bat = in.nextInt();
            if (bat >= 0){
                total = total + bat;
            }
            else {
                avg = avg - 1;
            }
        }
    System.out.println((float)total/(float)avg);
    }
}


import java.io.*;
public class Kattis {

    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        while (input != null) {

            String[] details = input.split(" ");
            String name = "";
            double average = 0;
            int total = 0;

            for (String detail : details) {

                if (detail.charAt(0) >= 'A' && detail.charAt(0) <= 'Z') {
                    name += detail + " ";
                } 

                else {
                    average = average + Double.parseDouble(detail);
                    total++;
                }

            }

            System.out.println((average / total) + " " + name);
            input = br.readLine();

        }

    }

}

mport java.util.Scanner;
public class Kattis { 
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNextLine()) {
            String line = in.nextLine();
            String [] array = line.split(" ");

            int sumof = 0;
            for (int i = 0; i < array.length; i ++) {
                sumof += Integer.valueOf(array[i]);
            }
            System.out.println(sumof / 2);
        }   
    }
}

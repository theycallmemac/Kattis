import java.util.Scanner;

public class Kattis{

     public static void main(String[] args){

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        int setNum = 1;

        while (n != 0){

            System.out.println("SET " + setNum);

            String[] names = new String[n];
            int num = n;

            for (int i = 0; i < n / 2; i++){

                names[i] = in.next();
                names[ num - 1] = in.next();
                num--;

            }

            if (n % 2 != 0) {
                names[(n / 2)] = in.next();
            }

            for (int i = 0; i < names.length; i++) {

                System.out.println(names[i]);

            }

            n = in.nextInt();

            setNum++;
       }
   }
}

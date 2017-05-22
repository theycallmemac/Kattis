import java.util.*;
import java.io.*;

class Kattis {

    public static void main(String[] args) throws Exception{
    
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        String input = br.readLine();
        while(input != null){
        
            int n = Integer.parseInt(input.trim());
            int sum = 1;
            for(int i = 2; i*i <= n; i++)
            {
                if(n % i == 0)
                {
                   sum += i;
                   int d = n/i;
                   if(d != i)
                      sum += d;
                }
            }

            if(sum == n)
                pw.println(n + " perfect");
            else if(Math.abs(sum - n) <= 2)
                pw.println(n + " almost perfect");
            else
                pw.println(n + " not perfect");

            input = br.readLine();

        }

        br.close();
        pw.close();
    
    }

}

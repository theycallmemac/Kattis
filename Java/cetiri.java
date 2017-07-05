import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Kattis{

     public static void main(String[] args){

        Scanner in = new Scanner(System.in);
        List<Integer> numbers = new ArrayList<>();

        int a = in.nextInt();
        numbers.add(a);
        int b = in.nextInt();
        numbers.add(b);
        int c = in.nextInt();
        numbers.add(c);

        Collections.sort(numbers);

        int firstDiff = numbers.get(1) - numbers.get(0);
        int secondDiff = numbers.get(2) - numbers.get(1);
        if(firstDiff > secondDiff){
           System.out.println(numbers.get(0) + secondDiff);
        }
        else if(firstDiff == secondDiff){
           System.out.println(numbers.get(2) + firstDiff);
        }
        else{
           System.out.println(numbers.get(1) + firstDiff);
        }

   }
}

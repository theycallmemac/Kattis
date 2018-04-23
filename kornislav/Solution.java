
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution {

    public static void main(String[] args) {

    	 List<Integer> stepsTaken = new ArrayList<Integer>();

        Scanner in = new Scanner(System.in);

		stepsTaken.add(in.nextInt());
		stepsTaken.add(in.nextInt());
		stepsTaken.add(in.nextInt());
		stepsTaken.add(in.nextInt());

		Collections.sort(stepsTaken);
		
		System.out.println(stepsTaken.get(0) * stepsTaken.get(2));


    }
}

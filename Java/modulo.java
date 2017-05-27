import java.util.Scanner;
import java.util.ArrayList;
public class Kattis {

  public static void main(String[] args) {
  Scanner scan = new Scanner(System.in);

  ArrayList<Integer> nums = new ArrayList<>();
  int zero = 0;

  for (int i = 0; i < 10; i++){
  
	test = scan.nextInt() % 42;
	if (!nums.contains(zero))
		nums.add(zero);
    
	}

  System.out.println(nums.size());

  scan.close();
	}

}

import java.util.Scanner;

public class Kattis {


  public static int get_max(int left, int right){
    if(left>right){
      return left;
    }
      return right;
  }


  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int left = in.nextInt();
    int right = in.nextInt();

    if(left == 0 && right == 0){
	     System.out.println("Not a moose");
    }
    else if(left == right){
	     System.out.println("Even "+ (left + right));
    }
    else{
	     System.out.println("Odd "+ 2 * get_max(left, right));
    }
  }
}

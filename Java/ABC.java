import java.util.Scanner;

public class Kattis {
	public static void main(String[]args){

		Scanner in = new Scanner(System.in);

		int x = in.nextInt();
		int y = in.nextInt();
		int z = in.nextInt();

		int a, b, c;

		if(x < y && x < z){

			a = x;
			if(y < z){
				b = y;
				c = z;
			}
			else{
				b = z;
				c = y;
			}

		}
		else if(y < z && y < x){

			a = y;
			if(x < z){
				b = x;
				c = z;
			}
			else{
				b = z;
				c = x;
			}

		}
		else{

			a = z;
			if(x < y){
				b = x;
				c = y;
			}
			else{
				b = y;
				c = x;

			}
		}
		in.nextLine();
		String line = in.nextLine();
		char first = line.charAt(0);
		char second = line.charAt(1);
		char third = line.charAt(2);
		int[] output = new int[3];
		if(first == 'A'){
			output[0] = a;
		}
		if(first == 'B'){
			output[0] = b;
		}
		if(first == 'C'){
			output[0] = c;
		}
		if(second == 'A'){
			output[1] = a;
		}
		if(second == 'B'){
			output[1] = b;
		}
		if(second == 'C'){
			output[1] = c;
		}
		if(third == 'A'){
			output[2] = a;
		}
		if(third == 'B'){
			output[2] = b;
		}
		if(third == 'C'){
			output[2] = c;
		}
		for(int i : output){
			System.out.print(i + " ");
		}
	}
}

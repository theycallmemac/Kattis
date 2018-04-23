
import java.util.Scanner;

class Kattis {

	public static void main(String [] args){

		int white = 0;
		int upper = 0;
		int lower = 0;
		int symbol = 0;

		Scanner in = new Scanner(System.in);
		String spam = in.next();

		for(int i = 0; i < spam.length(); i++){
			char character = spam.charAt(i);

			if(character == '_') {
				white++;
			}

			else if(character >= 'A' && character <= 'Z') {
				upper++;
			}

			else if(character >= 'a' && character <= 'z') {
				lower++;
			}

			else {
				symbol++;
			}

		}
		double total = white + upper + lower + symbol;

		System.out.println(white / total);
		System.out.println(lower / total);
		System.out.println(upper / total);
		System.out.println(symbol / total);

	}
}

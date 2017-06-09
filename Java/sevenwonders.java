
import java.util.Scanner;
import java.util.List;
import java.util.Arrays;
import java.util.Collections;

class Kattis {

	public static void main(String [] args){

		Scanner in = new Scanner(System.in);
		String cards = in.next();

		int array[]= new int[2];
		int tCount = 0;
		int cCount = 0;
		int gCount = 0;
		int setCount = 0;


		for(int i = 0; i < cards.length(); i++){
			char card = cards.charAt(i);
			if(card == "T".charAt(0)){
				tCount++;
			}

			if(card == "C".charAt(0)){
				cCount++;
			}

			if(card == "G".charAt(0)){
				gCount++;
			}
		}

		List<Integer> list = Arrays.asList(tCount,cCount,gCount);
		int min = Collections.min(list);

		if(min == 0){
			setCount = 0;
		}
		else {
			setCount = min * 7;
		}
		
		int total = (tCount * tCount)+(cCount * cCount)+( gCount * gCount) + setCount;
		System.out.println(total);


	}
}

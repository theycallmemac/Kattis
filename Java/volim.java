import java.util.Scanner;


public class Kattis {
	public static int getPerson(int n, int endGame, int counter, int person, int[] timesArray, String[] results){
		for(int i = 0; i < n; i++){
			counter = counter + timesArray[i];
			if(counter >= endGame){
				break;
			}
			else if(results[i].equals("T")){
				person++;
			}

			if(person > 8){
				person = person - 8;
			}
		}
		return person;
	}
	public static void main(String[] args){


		Scanner in = new Scanner(System.in);

		int k = in.nextInt();
		int n = in.nextInt();
		
		int endGame = 210;
		int counter = 0;
		int person = k;


		int[] timesArray = new int[n];
		String[] results = new String[n];

		for(int i = 0; i < n; i++){
			timesArray[i] = in.nextInt();
			results[i] = in.next();
		}


		int holder = getPerson(n, endGame,counter, person, timesArray, results);
		System.out.println(holder);
	}
}

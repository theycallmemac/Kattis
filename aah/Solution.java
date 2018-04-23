import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int says = br.readLine().length();
		int wants = br.readLine().length();
		

		if(wants <= says){
			System.out.println("go");
		}
		else{
			System.out.println("no");
		}
		
	} 
}

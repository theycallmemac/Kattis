
import java.util.Scanner;

public class Kattis {
	
	public static void main(String[] args){
		
		Scanner in = new Scanner(System.in);
		
		while(in.hasNext()){

			String input = in.nextLine();
			int len = input.length();
			char[] array = new char[26];
			
			for(int i=0; i < len; i++){
      
				array[input.charAt(i) - 'a']++;
        
			}

			int remove = 0;
			for(int i=0; i < array.length; i++){
      
				if((array[i]%2)==1) remove++;
        
			}
			
			if(remove > 0) remove--;
			System.out.print(remove);
      
		}
    
		in.close();
	}
  
}

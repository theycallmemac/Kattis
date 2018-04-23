
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        float gunnar = ( (in.nextFloat() + in.nextFloat() ) / 2) + ( (in.nextFloat() + in.nextFloat() ) / 2);
        float emma = ( (in.nextFloat() + in.nextFloat() ) / 2) + ( (in.nextFloat() + in.nextFloat() ) / 2);

        if(gunnar > emma){
            System.out.println("Gunnar");
        }

        else if(gunnar < emma){
            System.out.println("Emma");
        }
        
        else{
			      System.out.println("Tie");
		    }

    }
    
}

import java.util.Collections;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;


public class Kattis {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        Scanner scanner = new Scanner(System.in);
        
        int n = in.nextInt();
        
        List<String> arrayList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            arrayList.add(in.next());
        }
        
        List<String> list = new ArrayList<>(arrayList);
        List<String> array = new ArrayList<>(arrayList);
        Collections.sort(list);
        Collections.sort(array, Collections.reverseOrder());
        
        if(arrayList.equals(list)) {
            System.out.println("INCREASING");
        }
        else if(arrayList.equals(array)) {
            System.out.println("DECREASING");
        } 
        else {
            System.out.println("NEITHER");
        }
        
    }

}

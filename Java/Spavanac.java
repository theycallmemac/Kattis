import java.util.Scanner;

  public class Kattis {
  public static void main(String[] args) {
    final int dayMins = 60 * 24;
    final int hourMins = 60;

    Scanner in = new Scanner(System.in);
    int hours = in.nextInt();
    int mins = in.nextInt();

    int overMins = (hours * hourMins) + mins;
    int newMins = (overMins + dayMins - 45) % dayMins;
    int newHours = newMins / hourMins;
    newMins %= hourMins;
    System.out.println(String.format("%d %d", newHours, newMins));
  }
}

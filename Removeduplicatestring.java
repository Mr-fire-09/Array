import java.util.*;

public class Removeduplicatestring {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String input = sc.nextLine();

        // Using a HashMap to store unique characters
        HashMap<Character, Integer> map = new HashMap<>();
        for (char c : input.toCharArray()) {
            map.put(c, 1); // Store each character only once
        }

        // Print unique characters
        for (char key : map.keySet()) {
            System.out.print(key + " ");
        }

        sc.close();
    }
}

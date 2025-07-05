import java.util.*;

public class RemoveDuplicates {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input number of elements
        System.out.print("Enter the number of elements: ");
        int n = sc.nextInt();

        // Input array elements
        System.out.print("Enter the elements: ");
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            map.put(num, 1); // Store each element only once
        }

        // Print unique elements
        for (int key : map.keySet()) {
            System.out.print(key + " ");
        }

        sc.close();
    }
}

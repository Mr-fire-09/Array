import java.util.Scanner;

public class maxelemntarray {

    public static int find_max_element(int n, int arr[]) {
        int max = arr[0];
        for (int i : arr) {
            if (i > max) {
                max = i;
            }
        }
        return max;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number of elemnt :");
        int n = sc.nextInt();
        int arr[] = new int[n];

        System.out.println("Enter the elemnts :");
        for (int i : arr) {
            arr[i] = sc.nextInt();

        }

        int max = find_max_element(n, arr);

        System.out.println("max element " + max);

    }

}


public class countevennumber {

    public static void main(String[] args) {
        int count = 0;
        int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        for (int i : arr){
            if ( i % 2 == 0){
                count++;
            }
        
        }
        System.out.println("The count of even numbers in the array is: " + count);
    }
}
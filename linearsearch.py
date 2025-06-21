def linearSearch(n , arr, x):
    for i in arr:
        if i == x:
            return True
        
    return False


n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
x = int(input("Enter the element to search for: "))
y = linearSearch(n, arr, x)
print("Element found in the array." if y else "Element not found in the array.")
 
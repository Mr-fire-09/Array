n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
for i in range(n):
    print(arr[i], end=" ")
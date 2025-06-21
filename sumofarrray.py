def sumofarray(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
x = sumofarray(arr)
print("The sum of the array is:", x)
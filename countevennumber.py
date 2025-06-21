def countevennumber(arr):
    count = 0
    for i in arr:
        if i % 2 == 0:
            count += 1
            
    return count

n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
x = countevennumber(arr)
print("The count of even numbers in the array is:", x)
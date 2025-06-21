def binarysearch(n, arr,item):
    start = 0
    end = n -1
    mid = (start + end) // 2
    while (start <= end ):
        if (item == arr[mid]):
            return True
        elif (item > arr[mid]):
            start = mid + 1
            mid = (start + end) // 2
        else:
            end = mid - 1
            mid = (start + end) // 2
            
    return False
            
n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))
item = int(input("Enter the item to search: "))
print("Item found:", binarysearch(n, arr, item))
def selectionsort(n,arr):
    for i in range(0,n,1):
        for j in range(i+1,n,1):
            if (arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
                
    return arr



n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))
print("Sorted array:", selectionsort(n, arr))
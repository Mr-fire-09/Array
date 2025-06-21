def findMaxElemnt(n,arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max 

n = int(input())
arr = list(map(int,input().split()))
print(findMaxElemnt(n,arr))
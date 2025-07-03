s = "i love programming"
arr = s.split()
n = len(arr)
for i in range(n):
    arr[i] = arr[i][::-1]
arr = " ".join(arr)
print(arr)
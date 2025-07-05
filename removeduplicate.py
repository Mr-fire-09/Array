n  = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
# Remove duplicates from the list
d = {}
for i in arr:
    d[i] = 1
    
# Convert the dictionary keys back to a list
for k in d.keys():
    print(k, end=' ') 
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

# Count frequency of each element
d = {}
for i in arr:
    d[i] = d.get(i, 0) + 1

# Print frequencies
for k, v in d.items():
    print(k, "occurs", v, "times")

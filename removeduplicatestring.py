string = input("Enter a string: ")
d = {}
for i in string:
    d[i]= 0
# Convert the dictionary keys back to a list
for k in d.keys():
    print(k, end=' ')
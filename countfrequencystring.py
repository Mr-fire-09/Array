string = input("Enter a string: ")
d = {}

for i in string:
    d[i] = d.get(i, 0) + 1
    
for k, v in d.items():
    print(f"{k} occurs {v} times")

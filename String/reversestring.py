def  reverse(n,s):
    s = list(s)
    start = 0
    end = n - 1
    
    
    
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
        
    return "".join(s)


s = input("Enter a string: ")
n = len(s)
print(reverse(n, s))
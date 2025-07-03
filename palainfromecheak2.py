def reversestring(n,s):
    s1 = ""
    for i in range(n-1, -1, -1):
        s1 += s[i]
    return s == s1

s = input("Enter a string: ")
n = len(s)
if reversestring(n, s):
    print("Palindrome")
else:
    print("Not a Palindrome")
def is_palindrome(n, s):
    s = list(s)
    start = 0
    end = n - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
        
    return True

s = input("Enter a string: ")
n = len(s)

if is_palindrome(n, s):
    print("Palindrome")
else:
    print("Not a Palindrome")

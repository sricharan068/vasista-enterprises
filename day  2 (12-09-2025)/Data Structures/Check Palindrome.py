def isPalindrome(s):
    
    s=s.lower()
    a= s[::-1]
    if a==s:
        return True
    else:
        return False
s=str(input())
print(isPalindrome(s))

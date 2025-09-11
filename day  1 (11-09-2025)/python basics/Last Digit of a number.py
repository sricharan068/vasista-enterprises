#Given an integer n. Write a program to return the last digit of the numclass Solution:
def lastDigit(n):
    #Code here
    return abs(n) % 10

n=int(input())
print(lastDigit(n))

def printNos(n,i=1):
    if i<=n:
        print(i)
    printNos(n,i+1)
n=int(input())
printNos(n)

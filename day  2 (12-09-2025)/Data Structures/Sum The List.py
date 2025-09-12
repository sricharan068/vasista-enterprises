def listSum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum
if __name__== "__main__":
    arr=list(map(int, input().split()))
    print(arr)
    print(listSum(arr))

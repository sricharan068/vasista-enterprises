def decrementList(arr):
    #code here
    list=[]
    for i in arr:
        j=i-1
        list.append(j)
    return list
arr=list(map(int,input().split()))
print(decrementList(arr))

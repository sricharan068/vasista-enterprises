
class Solution:
    def modTask(N):
        if N<=1:
            return None
        return N//2+1
    N=int(input())
    k=modTask(N)
    print(k)
    
        

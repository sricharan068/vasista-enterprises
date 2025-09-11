n = int(input())
count=0
# Your code here
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print(True)
else:
    print(False)

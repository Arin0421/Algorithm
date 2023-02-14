import sys
input=sys.stdin.readline

k,n=map(int,input().split())
arr=[]
for _ in range(k):
    arr.append(int(input()))
arr.sort()

start=1
end=arr[-1]
result=0

while start<=end:
    cnt=0
    mid=(start+end)//2
    
    for i in range(k):
        cnt+=arr[i]//mid

    if cnt>=n:
        result=mid
        start=mid+1
    else:
        end=mid-1

print(result)

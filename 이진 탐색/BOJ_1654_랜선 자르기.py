import sys
k,n=map(int,input().split())
array=[int(sys.stdin.readline()) for _ in range(k)]

start=0
end=max(array)

result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    for x in array:
        if x>mid:
            total+=x//mid
    if total<n:
        end=mid-1
    else:
        result=mid
        start=mid+1
print(result)
    

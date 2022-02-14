import sys
k,n=map(int,input().split())
array=list(map(int,input().split()))

start=1
end=max(array)

result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    
    for x in array:
        if x>=mid:
            total+=x-mid
            
    if total>=n:
        result=mid
        start=mid+1
        
    else:
        end=mid-1
        
print(result)
    

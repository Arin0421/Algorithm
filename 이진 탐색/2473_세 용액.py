import sys

n=int(input())
arr=list(map(int,input().split()))

arr.sort()
min_take=sys.maxsize

for i in range(n-1):
    start=i+1
    end=n-1
    while start<end:
        take=arr[i]+arr[start]+arr[end]
        if abs(take)<min_take:
            min_take=abs(take)
            result=[arr[i],arr[start],arr[end]]
        if take<0:
            start+=1
        elif take>0:
            end-=1
        else:
            break

print(result[0],result[1],result[2])

import sys 
k,m=map(int,input().split())
array=[int(sys.stdin.readline())for _ in range(k)]

start=1
end = max(array)

result=0

while(start<=end):
    mid = (start + end)//2
    total=0
    
    for x in array:
        total += x//mid

    if total >= m:
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)

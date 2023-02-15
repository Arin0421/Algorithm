import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))

arr.sort()
min_result=sys.maxsize

left=0
right=n-1

while left<right:
    left_val=arr[left]
    right_val=arr[right]

    temp=left_val + right_val

    if abs(temp)<min_result:
        min_result=abs(temp)
        result=[left_val,right_val]
        if temp==0:
            break

    if temp<0:
        left+=1
    else:
        right-=1

print(result[0],result[1])

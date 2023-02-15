import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr.sort()

def b_search(start,end,m):

    while start<=end:
        mid = (start + end) // 2
        temp = 0
        for i in arr:
            if i<=mid:
                temp+=i
            else:
                temp+=mid
        if temp<=m:
            result=mid
            start=mid+1
        else:
            end=mid-1
    return result
if sum(arr)<=m:
    print(max(arr))
else:
    result=b_search(0,arr[-1],m)
    print(result)

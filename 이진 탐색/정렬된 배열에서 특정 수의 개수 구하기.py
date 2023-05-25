from bisect import bisect_left, bisect_right

def cnt(arr,x):
    left=bisect_left(arr,x)
    right=bisect_right(arr,x)

    return right-left

n,x=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

ans=cnt(arr,x)

print(ans if ans>0 else -1)

def b_search(arr,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return b_search(arr,target,start,mid-1)
    else:
        return b_search(arr,target,mid+1,end)

n=int(input())
arr=list(map(int,input().split()))
arr.sort()

m=int(input())
item=list(map(int,input().split()))

for i in item:
    result=b_search(arr,i,0,n-1)
    if result!=None:
        print("yes",end=' ')
    else:
        print("no",end=' ')

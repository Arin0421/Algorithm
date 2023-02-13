n=int(input())
data=list(map(int,input().split()))

def b_search(arr,start,end):
    if start>end:
        return None
    mid=(start+end)//2

    if arr[mid]==mid:
        return mid
    elif arr[mid]<mid:
        return b_search(arr,mid+1,end)
    else:
        return b_search(arr,start,mid-1)

result=b_search(data,0,n-1)

if result!=None:
    print(result)
else:
    print(-1)

n=int(input())
arr=list(map(int,input().split()))

arr.sort()
ans=1
idx=0
while True:
    if ans<arr[idx]:
        break
    ans+=arr[idx]
    idx+=1

print(ans)

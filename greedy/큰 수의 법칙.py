n,m,k=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort(reverse=True)

result=0
cnt=0
for _ in range(m):
    if cnt==k:
        result+=arr[1]
        cnt=0
    else:
        result+=arr[0]
        cnt+=1
print(result)

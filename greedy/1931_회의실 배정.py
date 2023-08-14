n=int(input())
arr=[]

for _ in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))

arr=sorted(arr, key=lambda x:(x[1],x[0]))

start=arr[0][1]
ans=1

for i in range(1,n):
    if arr[i][0] >= start:
        start = arr[i][1]
        ans += 1

print(ans)

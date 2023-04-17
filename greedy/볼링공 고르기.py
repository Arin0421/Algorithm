from itertools import combinations

n,m=map(int,input().split())
data=list(map(int,input().split()))

arr=list(combinations(data,2))
ans=len(arr)

for i,j in arr:
    if i==j:
        ans-=1

print(ans)

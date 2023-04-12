n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()
ans=0
cnt=0

for _ in range(m):
    if cnt==k:
        ans+=data[-2]
        cnt=0
        continue
    ans+=data[-1]
    cnt+=1

print(ans)

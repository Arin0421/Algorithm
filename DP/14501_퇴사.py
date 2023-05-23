n=int(input())
t=[0,]
p=[0,]
for _ in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)

dp=[0]*(n+2)

for i in range(n,-1,-1):
    if t[i]+i<=n+1:
        dp[i]=p[i]+max(dp[i+t[i]:])

print(max(dp))

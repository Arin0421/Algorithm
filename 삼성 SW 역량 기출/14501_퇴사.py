n=int(input())
t=[]
p=[]

for _ in range(n):
    i,j=map(int,input().split())
    t.append(i)
    p.append(j)

dp=[0]*(n+1)

for i in range(n-1,-1,-1):
    print(i)
    day = t[i]+i
    if day <= n:
        dp[i]=max(dp[day:])+p[i]

print(max(dp))

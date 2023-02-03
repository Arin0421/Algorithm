import sys
input=sys.stdin.readline

n,k=map(int,input().split())
c=[]
for i in range(n):
    c.append(int(input()))

dp=[100001]*(k+1)
dp[0]=0
for i in c:
    for j in range(i,k+1):
        dp[j]=min(dp[j-i]+1,dp[j])

if dp[k]==100001:
    print(-1)
else:
    print(dp[k])

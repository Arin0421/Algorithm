import sys
input=sys.stdin.readline

c,n=map(int,input().split())
costs=[list(map(int,input().split())) for _  in range(n)]
dp=[1e7]*(c+100)
dp[0]=0

for cost,num in costs:
    for i in range(num,c+100):
        dp[i]=min(dp[i-num]+cost,dp[i])

print(min(dp[c:]))

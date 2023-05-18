n=int(input())
s=[0]
s+=list(map(int,input().split()))
dp=[10001]*1001

dp[1]=s[1]
dp[2]=min(dp[1]*2,s[2])

for i in range(3,n+1):
    dp[i]=s[i]
    for j in range(1,i//2+1):
        dp[i]=min(dp[i],dp[j]+dp[i-j])

print(dp[n])

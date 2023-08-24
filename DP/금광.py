t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))

    dp=[]
    idx=0
    for i in range(n):
        dp.append(arr[idx:idx+m])
        idx+=m

    for i in range(1,m):
        for j in range(n):
            if j==0:
                dp[j][i]+=max(dp[j][i-1],dp[j+1][i-1])
            elif j==n-1:
                dp[j][i]+=max(dp[j][i-1],dp[j-1][i-1])
            else:
                dp[j][i]+=max(dp[j-1][i-1],dp[j][i-1],dp[j+1][i-1])

    ans=0
    for i in range(n):
        ans=max(ans,dp[i][m-1])
    print(ans)

from copy import deepcopy

n=int(input())
arr=[[0,0]]

for _ in range(n-1):
    a,b=map(int,input().split())
    arr.append((a,b))
k=int(input())
if n==1:
    print(0)
    exit()
elif n==2:
    print(arr[1][0])
    exit()
    
dp=[0]*(n+1)
dp[2]=arr[1][0]
dp[3]=min(arr[1][0]+arr[2][0],arr[1][1])
for i in range(4,n+1):
    dp[i]=min(dp[i-1]+arr[i-1][0],dp[i-2]+arr[i-2][1])



min_val=int(1e9)
for i in range(1,n-2):
    dp2=deepcopy(dp)
    if dp[i]+k<dp[i+3]:
        dp2[i+3]=dp2[i]+k
        for j in range(i+4,n+1):
            dp2[j]=min(dp2[j],dp2[j-1]+arr[j-1][0],dp2[j-2]+arr[j-2][1])
        if min_val>dp2[-1]:
            min_val=dp2[-1]
if min_val==int(1e9):
    print(dp[-1])
else:
    print(min_val)

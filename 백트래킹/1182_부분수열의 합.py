import sys
input=sys.stdin.readline

n,s=map(int,input().split())
arr=list(map(int,input().split()))
ans=0

def dfs(idx,num):
    global ans

    if idx>=n:
        return

    num+=arr[idx]

    if num==s:
        ans+=1

    dfs(idx+1,num)

    dfs(idx+1,num-arr[idx])

dfs(0,0)
print(ans)

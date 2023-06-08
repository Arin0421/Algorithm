n,k=map(int,input().split())
kit=list(map(int,input().split()))
visited=[False]*n

ans=0
def back(wei,cnt):
    global ans

    if cnt==n:
        ans+=1
        return

    for i in range(n):
        if wei-k+kit[i]>=500 and not visited[i]:
            visited[i]=True
            back(wei-k+kit[i],cnt+1)
            visited[i]=False

back(500,1)

print(ans)

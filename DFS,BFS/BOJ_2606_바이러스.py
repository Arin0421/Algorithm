
def dfs(v):
    global sum
    visited[v]=True
    for e in adj[v]:
        if not visited[e]:
            sum+=1
            dfs(e)

n=int(input())
k=int(input())
adj=[[] for _ in range(n+1)]
     
result=[]
     
for _ in range(k):
     x,y=map(int,input().split())
     adj[x].append(y)
     adj[y].append(x)
sum=0
visited=[False]*(n+1)
dfs(1)

print(sum)

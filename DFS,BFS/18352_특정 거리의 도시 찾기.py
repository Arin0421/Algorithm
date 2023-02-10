from collections import deque

n,m,k,x=map(int,input().split())
graph = [ [] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

dist=[-1]*(n+1)
dist[x]=0

def bfs(s):
    q=deque([s])
    while q:
        v=q.popleft()
        for i in graph[v]:
            if dist[i]==-1:
                dist[i]=dist[v]+1
                q.append(i)

check=False
bfs(x)

for i in range(1,n+1):
    if dist[i]==k:
        print(i)
        check=True
if check==False:
    print(-1)

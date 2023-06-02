import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[ [INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][j])

ans=[]
m_val=max(graph[1][1:])
cnt=0
for i in range(1,n+1):
    if graph[1][i]==m_val:
        ans.append(i)
        break
ans.append(m_val)
ans.append(graph[1].count(m_val))

print(*ans)

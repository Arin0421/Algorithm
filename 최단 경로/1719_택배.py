import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[ [INF]*(n+1) for _  in range(n+1)]
ans=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
            ans[i][j]=INF

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c
    graph[b][a]=c
    ans[a][b]=b
    ans[b][a]=a

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j]=graph[i][k]+graph[k][j]
                ans[i][j]=ans[i][k]

for i in range(1,n+1):
    for j in range(1,n+1):
        if ans[i][j]==INF:
            print('-',end=' ')
        else:
            print(ans[i][j],end=' ')
    print()

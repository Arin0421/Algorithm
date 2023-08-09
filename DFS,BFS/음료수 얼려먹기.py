from collections import deque

n,m=map(int,input().split())
graph=[list(map(int,input())) for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    graph[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]=1
                q.append((nx,ny))
    return True

ans=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            bfs(i,j)
            ans+=1

print(ans)

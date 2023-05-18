from collections import deque

m,n=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
dist=[[-1]*m for _ in range(n)]
dist[0][0]=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if dist[nx][ny]==-1:
                    if graph[nx][ny]==0:
                        dist[nx][ny]=dist[x][y]
                        q.appendleft((nx,ny))
                    else:
                        dist[nx][ny]=dist[x][y]+1
                        q.append((nx,ny))
    return dist[n-1][m-1]
print(bfs(0,0))

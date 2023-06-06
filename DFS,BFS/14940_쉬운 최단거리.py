from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]

distance=[[-1]*m for _ in range(n)]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    distance[x][y]=0
    while q:
        a,b=q.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if distance[nx][ny]==-1 and graph[nx][ny]==1:
                    distance[nx][ny]=distance[a][b]+1
                    q.append((nx,ny))

x,y=0,0
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            x=i
            y=j

bfs(x,y)
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            distance[i][j]=0

for i in distance:
    print(*i)

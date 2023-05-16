from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0:
                    q.append((nx,ny))
                    graph[nx][ny]=graph[x][y]+1


m,n=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

q=deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            q.append((i,j))

bfs()
result=0

for i in graph:
    if 0 in i:
        print(-1)
        exit()
    result=max(result,max(i))

print(result-1)

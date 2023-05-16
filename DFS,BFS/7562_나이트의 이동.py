from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,-2,-2,-1,1,2,2,1]
dy=[-2,-1,1,2,-2,-1,1,2]

def bfs(x,y,a,b):
    q=deque()
    q.append((x,y))
    graph[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==0:
                    q.append((nx,ny))
                    graph[nx][ny]=graph[x][y]+1
    return graph[a][b]

t=int(input())
for _ in range(t):
    n=int(input())
    graph=[[0]*n for _ in range(n)]
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    print(bfs(x,y,a,b)-1)

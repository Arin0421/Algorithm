import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
graph=[ list(map(int,input().split())) for _ in range(n)]
s,x,y=map(int,input().split())
data=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(target,rx,ry):
    while q:
        virus,s,x,y=q.popleft()
        if s==target:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
                graph[nx][ny]=virus
                q.append((virus,s+1,nx,ny))
    return graph[rx-1][ry-1]
        
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            data.append((graph[i][j],0,i,j))
data.sort()
q=deque(data)

print(bfs(s,x,y))

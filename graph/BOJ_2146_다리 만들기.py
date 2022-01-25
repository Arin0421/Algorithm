import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    graph[x][y]=0
    cnt=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==0:
                    cnt+=1
                    graph[nx][ny]=1
                    q.append((nx,ny))
    return cnt
                        
                    

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            result=bfs(i,j)
            print(result)
    
    

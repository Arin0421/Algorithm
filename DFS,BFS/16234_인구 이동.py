import sys
from collections import deque
input=sys.stdin.readline

n,l,r=map(int,input().split())
graph=[ list(map(int,input().split())) for _ in range(n) ]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(a,b):
    q=deque()
    q.append((a,b))
    temp=[]
    temp.append((a,b))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if l<=abs(graph[x][y]-graph[nx][ny])<=r:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    temp.append((nx,ny))
    return temp

result=0
while 1:
    visited = [[0]*(n+1) for _ in range(n+1)]
    flag=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                visited[i][j]=1
                country=bfs(i,j)
                if len(country)>1:
                    flag=1
                    num=sum(graph[x][y] for x,y in country)//len(country)
                    for x,y in country:
                        graph[x][y]=num
    if flag==0:
        break
    result+=1

print(result)

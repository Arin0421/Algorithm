import sys
from collections import deque
input=sys.stdin.readline

n,m,t=map(int,input().split())
graph=[ list(map(int,input().split())) for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y,w,z,time):
    q=deque()
    q.append((x,y,time))
    visited=[[0]*m for _ in range(n)]
    while q:
        x,y,time=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]!=1 and not visited[nx][ny]:
                if nx==w and ny==z:
                    return time+1
                visited[nx][ny]=1
                q.append((nx,ny,time+1))
    return 10**6

for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            a,b=i,j
case1=bfs(0,0,n-1,m-1,0)
temp=bfs(0,0,a,b,0)
if temp!=False:
    case2=temp+abs(n-1-a)+abs(m-1-b)
else:
    case2=temp

result=min(case1,case2)
print(result if result<=t else 'Fail')

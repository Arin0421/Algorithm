from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    cnt=1
    graph[x][y]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
                q.append((nx,ny))
                cnt+=1
                graph[nx][ny]=0
    return cnt

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

ans=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            ans.append(bfs(i,j))

ans.sort()
print(len(ans))
for i in ans:
    print(i)

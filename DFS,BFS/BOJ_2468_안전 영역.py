from collections import deque

n=int(input())
graph=[]
maxNum=0
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        maxNum=max(graph[i][j],maxNum)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,height,visited):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]>height and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    queue.append((nx,ny))

result = 0
for k in range(maxNum):
    visited = [ [0]*n for _ in range(n)]
    cnt=0

    for i in range(n):
        for j in range(n):
            if graph[i][j]>k and visited[i][j]==0:
                bfs(i,j,k,visited)
                cnt+=1
    result=max(result,cnt)

print(result)

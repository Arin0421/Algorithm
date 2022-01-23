from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
queue=deque([])

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1:
                    graph[nx][ny]=graph[x][y]+1
                    queue.append([nx,ny])
    return graph[n-1][m-1]
            

print(bfs(0,0))

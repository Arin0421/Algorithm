from collections import deque

n,l,r=map(int,input().split())
world=[list(map(int,input().split())) for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    temp=[]
    temp.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if l<=abs(world[x][y]-world[nx][ny])<=r:
                    visited[nx][ny]=True
                    q.append((nx,ny))
                    temp.append((nx,ny))
    return temp

ans=0
while 1:
    visited = [[False] * (n) for _ in range(n)]
    flag=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:
                visited[i][j]=True
                country=bfs(i,j)
                if len(country)>1:
                    flag=1
                    num=sum(world[x][y] for x,y in country)//len(country)
                    for x,y in country:
                        world[x][y]=num
    if flag==0:
        break
    ans+=1

print(ans)

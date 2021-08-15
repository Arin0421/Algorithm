import sys
sys.setrecursionlimit(10**6)

graph=[]
t=int(input())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y):
    graph[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
            dfs(nx,ny)
            
for _ in range(t):
    m,n,k=map(int,input().split())

    graph=[[0]*m for _ in range(n)]

    for _ in range(k):
        a,b=map(int,input().split())
        graph[b][a]=1
    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                dfs(i,j)
                cnt+=1
    print(cnt)



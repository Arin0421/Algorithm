import sys
sys.setrecursionlimit(100000)

def dfs(y,x):
    global cnt
    graph[y][x]=1
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0 <= ny < m and 0 <= nx < n and graph[ny][nx]==0:
            cnt+=1
            dfs(ny,nx)

m,n,k=map(int,input().split())

graph=[[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j]=1
            
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt=1
area=0
result=[]

for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            area+=1
            dfs(i,j)
            result.append(cnt)
            cnt=1

result.sort()
print(area)
print(' '.join(map(str,result)))

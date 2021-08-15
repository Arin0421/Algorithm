graph=[]
n=int(input())
result=[]

dx=[0,0,1,-1]
dy=[1,-1,0,0]
cnt=0

for _ in range(n):
    x=list(map(int,input()))
    graph.append(x)

def dfs(x,y):
    global cnt
    graph[x][y]=0
    cnt+=1
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
            dfs(nx,ny)
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt=0
            result.append(dfs(i,j))
print(len(result))
result.sort()

for i in result:
    print(i)

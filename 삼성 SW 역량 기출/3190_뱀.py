import sys
input=sys.stdin.readline

n=int(input())
k=int(input())
graph=[[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a,b=map(int,input().split())
    graph[a][b]=1
l=int(input())
info=[]
for _ in range(l):
    x,c=map(str,input().split())
    info.append((int(x),c))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(dir,c):
    if c=='L':
        dir=(dir-1)%4
    else:
        dir=(dir+1)%4
    return dir

def simul():
    x,y=1,1
    graph[x][y]=2
    dir=0
    time=0
    idx=0
    snake=[(x,y)]

    while True:
        nx=x+dx[dir]
        ny=y+dy[dir]

        if 0<nx<=n and 0<ny<=n and graph[nx][ny]!=2:
            if graph[nx][ny]==0:
                graph[nx][ny]=2
                snake.append((nx,ny))
                px,py=snake.pop(0)
                graph[px][py]=0
            else:
                graph[nx][ny]=2
                snake.append((nx,ny))
        else:
            time+=1
            break

        x,y=nx,ny
        time+=1
        if idx<l and time==info[idx][0]:
            dir=turn(dir,info[idx][1])
            idx+=1
    return time

print(simul())

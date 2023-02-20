n,m=map(int,input().split())
graph=[]
x,y,dir=map(int,input().split())
d=[[0]*m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global dir
    dir-=1
    if dir==-1:
        dir=3

cnt=0
turn=0
while True:
    turn_left()
    nx=x+dx[dir]
    ny=y+dy[dir]
    if d[nx][ny]==0 and graph[nx][ny]==0:
        d[nx][ny]=1
        x=nx
        y=ny
        cnt+=1
        turn=0
        continue
    else:
        turn+=1
    if turn==4:
        nx=x-dx[dir]
        ny=y-dy[dir]
        if graph[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn=0

print(cnt)

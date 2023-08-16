n=int(input())
k=int(input())
board=[[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a,b=map(int,input().split())
    board[a][b]=1

info=[]
l=int(input())
for _ in range(l):
    a,b=input().split()
    info.append((int(a),b))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(dir,c):
    if c=='L':
        dir=(dir-1)%4
    else:
        dir=(dir+1)%4
    return dir

x,y=1,1
board[x][y]=2
time=0
dir=0
idx=0
q=[(x,y)]
while True:
    nx=x+dx[dir]
    ny=y+dy[dir]
    if 1<=nx<=n and 1<=ny<=n and board[nx][ny]!=2:
        if board[nx][ny]==0:
            board[nx][ny]=2
            q.append((nx,ny))
            px,py=q.pop(0)
            board[px][py]=0
        if board[nx][ny]==1:
            board[nx][ny]=2
            q.append((nx,ny))
    else:
        time+=1
        break
    x,y=nx,ny
    time+=1
    if idx<l and time==info[idx][0]:
        dir=turn(dir,info[idx][1])
        idx+=1

print(time)

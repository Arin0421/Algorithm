from itertools import combinations

n=int(input())
graph=[list(map(str,input().split())) for _ in range(n)]
temp=[['S']*n for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

empty=[]
teacher=0
for i in range(n):
    teacher+=graph[i].count('T')
    for j in range(n):
       if graph[i][j]=='X':
           empty.append((i,j))

idxs=list(combinations(empty,3))

def bfs(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        while 0<=nx<n and 0<=ny<n and temp[nx][ny]!='O':
            if graph[nx][ny]=='S':
                return True
            else:
                nx+=dx[i]
                ny+=dy[i]
    return False

for idx in idxs:
    for i in range(n):
        for j in range(n):
            temp[i][j]=graph[i][j]
    for x,y in idx:
        temp[x][y]='O'

    cnt=0
    for i in range(n):
        for j in range(n):
            if temp[i][j]=='T':
                if not bfs(i,j):
                    cnt+=1

    if cnt==teacher:
        print('YES')
        exit(0)

print('NO')

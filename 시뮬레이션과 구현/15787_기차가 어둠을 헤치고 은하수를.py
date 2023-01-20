import sys
input = sys.stdin.readline

n,m=map(int,input().split())

trains = [ [0]*20 for _ in range(n) ]

for _ in range(m):
    a=list(map(int,input().split()))
    
    if a[0]==1:
        trains[a[1]-1][a[2]-1]=1
    elif a[0]==2:
        trains[a[1]-1][a[2]-1]=0
    elif a[0]==3:
        for j in range(19,0,-1):
            trains[a[1]-1][j]=trains[a[1]-1][j-1]
        trains[a[1]-1][0]=0
    elif a[0]==4:
        for j in range(19):
            trains[a[1]-1][j]=trains[a[1]-1][j+1]
        trains[a[1]-1][19]=0

cnt=0
state=[]
for i in range(n):
    if trains[i] not in state:
        state.append(trains[i])
        cnt+=1

print(cnt)

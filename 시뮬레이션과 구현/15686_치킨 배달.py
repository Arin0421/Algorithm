from itertools import combinations
n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
answer=1e9

house=[]
chick=[]
for i in range(n):
    for j in range(n):
        if maps[i][j]==2:
            chick.append((i,j))
        elif maps[i][j]==1:
            house.append((i,j))

for c in combinations(chick,m):
    total=0
    for x1,y1 in house:
        distance=1e9
        for x2,y2 in c:
            distance=min(distance,abs(x1-x2)+abs(y1-y2))
        total+=distance
    answer=min(answer,total)

print(answer)

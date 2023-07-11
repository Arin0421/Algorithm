import sys
from itertools import combinations
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

chi=[]
house=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            chi.append((i,j))
        elif graph[i][j]==1:
            house.append((i,j))

def dis(x,y,a,b):
    res=abs(x-a)+abs(y-b)
    return res

ans=1e9
for c in combinations(chi,m):
    total=0
    for x,y in house:
        distance=1e9
        for a,b in c:
            distance=min(distance,dis(x,y,a,b))
        total+=distance
    ans=min(ans,total)

print(ans)

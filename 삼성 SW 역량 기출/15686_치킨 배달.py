from itertools import combinations
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

def chik_distance(hx,hy,cx,cy):
    return abs(hx-cx)+abs(hy-cy)

c=[]
p=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            c.append((i,j))
        if graph[i][j]==1:
            p.append((i,j))
ans=1e9
for chick in list(combinations(c,m)):
    temp=0
    for px,py in p:
        distance=1e9
        for cx,cy in chick:
            distance=min(distance,chik_distance(px,py,cx,cy))
        temp+=distance
    ans=min(temp,ans)

print(ans)

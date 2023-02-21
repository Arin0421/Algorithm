import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)
n,m,c=map(int,input().split())

graph=[ [] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

def dijk(c):
    q=[]
    heapq.heappush(q,(0,c))
    distance[c]=0
    while q:
        dist,now=heapq.heappop(q)
        for i in graph[now]:
            if distance[now]<dist:
                continue
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijk(c)
num,time=-1,0
for i in range(1,n+1):
    if distance[i]!=INF:
        num+=1
        time=max(time,distance[i])
print(num,time)

import heapq
import sys
input=sys.stdin.readline
INF = sys.maxsize

n,w=map(int,input().split())
m=float(input())
data=[[0,0]]
graph=[ [] for _ in range(n+1)]

def get_distance(x1,y1,x2,y2):
    return (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5

for _ in range(n):
    x,y=map(int,input().split())
    data.append((x,y))

for i in range(1,n+1):
    for j in range(i+1,n+1):
        dist = get_distance(data[i][0],data[i][1],data[j][0],data[j][1])
        if dist <= m:
            graph[i].append((j,dist))
            graph[j].append((i, dist))

for _ in range(w):
    a,b=map(int,input().split())
    graph[a].append((b,0))
    graph[b].append((a,0))
distance=[INF]*(n+1)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(1)

print(int(distance[n]*1000))

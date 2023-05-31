import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for _ in range(m):
    a, b, time = map(int, input().split())
    if graph[a-1][b-1] <= time:
        print('Enjoy other party')
    else:
        print('Stay here')

"""
다익스트라를 이용한 풀이
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
data=[ list(map(int,input().split())) for _ in range(n)]
graph= [ [] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if data[i][j]==0:
            continue
        else:
            graph[i].append((j,data[i][j]))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

for _ in range(m):
    a,b,c=map(int,input().split())
    distance = [INF] * n
    dijkstra(a-1)
    if distance[b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")
"""

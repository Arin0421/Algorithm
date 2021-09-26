import heapq
import sys
input=sys.stdin.readline
INF = (1e9)

T=int(input())
def dijkstra(s):
    distance = [INF] * (n+1)
    q=[]
    heapq.heappush(q,(0,s))
    distance[s]=0
    while q :
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

for _ in range(T):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    graph= [ [] for i in range(n+1)]
    
    result=[]

    for _ in range(m):
        a,b,d=map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))


    ex=[]
    for k in range(t):
        ex.append(int(input()))
    original = dijkstra(s)
    g_distance = dijkstra(g)
    h_distance = dijkstra(h)

    for i in ex:
        if original[g]+g_distance[h]+h_distance[i] == original[i] or original[h]+h_distance[g]+g_distance[i] == original[i]:
            result.append(i)
    result.sort()
    for f in result:
        print(f,end=" ")
    print()



  
                


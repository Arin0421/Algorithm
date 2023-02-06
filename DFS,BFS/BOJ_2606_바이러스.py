from collections import deque
n=int(input())
con=int(input())

graph= [ [] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(con):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

num=0
q=deque([1])
visited[1]=True

while q:
    v=q.popleft()
    for i in graph[v]:
        if not visited[i]:
            q.append(i)
            visited[i]=True
            num+=1

print(num)

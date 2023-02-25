from collections import deque

n,m=map(int,input().split())
graph= [ [] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

first,second=map(int,input().split())
def bfs(weight):
    q=deque()
    visited=[False]*(n+1)
    q.append(first)
    visited[first]=True

    while q:
        x=q.popleft()
        for next, w in graph[x]:
            if not visited[next] and w>=weight:
                visited[next]=True
                q.append(next)

    if visited[second]:
        return True
    else:
        return False

start=1
end=1e9

result=0
while start<=end:
    mid=(start+end)//2

    if bfs(mid):
        start=mid+1
        result=mid
    else:
        end=mid-1

print(int(result))

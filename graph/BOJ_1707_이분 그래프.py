import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    visited[x]=1
    q=deque()
    q.append(x)
    while q:
        a=q.popleft()
        for i in graph[a]:
            if visited[i]==0:
                visited[i]=-visited[a]
                q.append(i)
            else:
                if visited[i]==visited[a]:
                    return False
    return True


k=int(input())

for i in range(k):
    v,e=map(int,input().split())
    isTrue = True
    graph=[ [] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    result=1
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for k in range(1,v+1):
        if visited[k]==0:
            if not bfs(k):
                result=-1
                break
    print("YES" if result==1 else "NO")

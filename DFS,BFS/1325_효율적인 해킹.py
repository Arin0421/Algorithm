import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[ [] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)

def bfs(s):
    num=1
    visited=[False]*(n+1)
    
    q=deque([s])
    visited[s]=True
    while q:
        v=q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
                num+=1
    return num

maxCnt=0
result=[]

for i in range(1,n+1):
	cnt = bfs(i)
	if cnt > maxCnt:
		maxCnt = cnt
		result.clear()
		result.append(i)
	elif cnt == maxCnt:
		result.append(i)

print(*result)

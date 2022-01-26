from collections import deque

v = int(input())

tree = [[] for _ in range(v+1)]

for _ in range(v):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-1, 2):
        tree[temp[0]].append((temp[i], temp[i+1]))

def bfs(n):
    visited=[-1]*(v+1)
    q=deque()
    q.append(n)
    visited[n]=0

    _max=[0,0]
    
    while q:
        par=q.popleft()
        for ch in tree[par]:
            if visited[ch[0]]==-1:
                visited[ch[0]]=visited[par]+ch[1]
                q.append(ch[0])

                if _max[0]<visited[ch[0]]:
                    _max[0]=visited[ch[0]]
                    _max[1]=ch[0]
    return _max

value,node=bfs(1)
result,node2=bfs(node)
print(result)

import sys
sys.setrecursionlimit(10**7)

def dfs(v):
    global result
    visited[v]=1
    cycle.append(v)

    next=graph[v]
    if visited[next]==0:
        dfs(next)
    else:
        if next in cycle:
            result+=cycle[cycle.index(next):]
    
        
t=int(input())

for _ in range(t):
    n=int(input())
    graph=[0]+list(map(int,input().split()))
    visited=[0]*(n+1)
    result=[]

    for i in range(1,n+1):
        if visited[i]==0:
            cycle=[]
            dfs(i)

    print(n-len(result))

n,m=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
visited=[False]*n
temp,ans=[],set()

def dfs():
    if len(temp)==m:
        ans.add(tuple(temp))
        return
    for i in range(n):
        if visited[i]:
            continue
        temp.append(data[i])
        visited[i]=True
        dfs()
        visited[i]=False
        temp.pop()

dfs()
for i in sorted(ans):
    print(*i)

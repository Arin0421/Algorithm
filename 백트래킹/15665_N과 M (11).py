n,m=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
temp,ans=[],set()

def dfs():
    if len(temp)==m:
        ans.add(tuple(temp))
        return
    for i in range(n):
        temp.append(data[i])
        dfs()
        temp.pop()

dfs()
for i in sorted(ans):
    print(*i)

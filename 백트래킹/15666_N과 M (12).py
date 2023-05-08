n,m=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
temp,ans=[],set()

def dfs():
    if len(temp)==m:
        ans.add(tuple(temp))
        return
    for i in range(n):
        if len(temp)==0 or temp[-1]<=data[i]:
            temp.append(data[i])
            dfs()
            temp.pop()

dfs()
for i in sorted(ans):
    print(*i)

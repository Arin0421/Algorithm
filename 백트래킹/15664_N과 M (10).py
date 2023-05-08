n,m=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
temp,ans=[],set()

def dfs(idx):
    if len(temp)==m:
        ans.add(tuple(temp))
        return
    for i in range(idx,n):
        temp.append(data[i])
        dfs(i+1)
        temp.pop()

dfs(0)
for i in sorted(ans):
    print(*i)

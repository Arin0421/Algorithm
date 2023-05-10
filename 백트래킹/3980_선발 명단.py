
def dfs(player,score):
    global max_score
    if player==11:
        max_score=max(max_score,score)
        return
    for i in range(11):
        if visited[i] or not data[player][i]:
            continue
        visited[i]=1
        dfs(player+1,score+data[player][i])
        visited[i]=0

t=int(input())
for _ in range(t):
    data=[list(map(int,input().split())) for _ in range(11)]
    max_score=0
    visited=[0]*11
    dfs(0,0)
    print(max_score)

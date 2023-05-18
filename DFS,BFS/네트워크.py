def solution(n, computers):
    answer = 0
    visit=[0]*n
    
    def dfs(x):
        visit[x]=1
        for i in range(n):
            if i!=x and computers[x][i]==1:
                if visit[i]==0:
                    visit[i]=1
                    dfs(i)
    for i in range(n):
        if visit[i]==0:
            dfs(i)
            answer+=1
            
    return answer

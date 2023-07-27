INF=int(1e9)
def solution(n, s, a, b, fares):
    answer = INF
    graph=[[INF]*(n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(n+1):
            if i==j:
                graph[i][j]=0
    
    for i,j,k in fares:
        graph[i][j]=k
        graph[j][i]=k
        
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
                
    for k in range(1,n+1):
        temp=graph[s][k]+graph[k][a]+graph[k][b]
        answer=min(temp,answer)
    
    return answer

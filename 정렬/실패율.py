def solution(N, stages):
    answer = []
    now=[0]*(N+2)
    
    for i in stages:
        now[i]+=1
    
    for i in range(1,N+1):
        if now[i]==0:
            answer.append((i,0))
        else:
            answer.append((i,now[i]/sum(now[i:])))
    
    answer=sorted(answer,key=lambda x:-x[1])
    
    for i in range(N):
        answer[i]=answer[i][0]
    
    return answer

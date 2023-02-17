def solution(n, stages):
    answer = []
    now=[0]*(n+2)
    for i in stages:
        now[i]+=1
    
    for i in range(1,n+1):
        if now[i]==0:
            answer.append((i,0))
        else:
            answer.append((i,now[i]/sum(now[i:])))
    answer=sorted(answer,key=lambda x:-x[1])
    
    for i in range(n):
        answer[i]=answer[i][0]
        
    return answer

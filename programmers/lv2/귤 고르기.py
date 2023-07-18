def solution(k, tangerine):
    answer = 0
    
    n=len(tangerine)
    
    d=dict()
    for i in tangerine:
        if i not in d:
            d[i]=0
        d[i]+=1
        
    d=sorted(d.items(),key=lambda x:-x[1])
    
    for key,value in d:
        if k<=0:
            break
        k-=value
        answer+=1
        
    return answer

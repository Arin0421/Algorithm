def solution(clothes):
    answer = 1
    coni={}
    for c in clothes:
        if c[1] not in coni:
            coni[c[1]]=0
        coni[c[1]]+=1
    
    for i in coni.values():
        answer*=(i+1)
    
    answer-=1
    
    return answer

def solution(s):
    answer = ''
    
    re=list(map(int,s.split()))
    answer+=str(min(re))+' '+str(+max(re))
    
    return answer

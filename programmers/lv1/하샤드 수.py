def solution(x):
    answer = True
    num=str(x)
    has_num=0
    for i in num:
        has_num+=int(i)
        
    if x%has_num!=0:
        answer=False
    return answer

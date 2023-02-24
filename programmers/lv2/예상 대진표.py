from math import ceil
def solution(n,a,b):
    answer = 1
    
    for i in range(n):
        if abs(a-b)==1 and max(a,b)%2==0:
            break
        a=ceil(a/2)
        b=ceil(b/2)
        answer+=1
    return answer

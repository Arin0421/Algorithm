from collections import Counter

def solution(topping):
    answer = 0
    
    h=Counter(topping)
    d=set()
    
    for i in topping:
        h[i]-=1
        d.add(i)
        if h[i]==0:
            h.pop(i)
        if len(h)==len(d):
            answer+=1
    return answer

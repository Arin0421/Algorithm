def solution(s):
    re=[ int(a) for a in s.split()]
    answer=[]
    answer.append(str(min(re)))
    answer.append(str(max(re)))
    return " ".join(answer)

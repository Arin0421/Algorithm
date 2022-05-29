def solution(strings, n):
    answer = []
    li=[]
    for st in strings:
        li.append(st[n]+st)
    li.sort()
    
    for i in range(len(strings)):
        answer.append(li[i][1:])
    return answer

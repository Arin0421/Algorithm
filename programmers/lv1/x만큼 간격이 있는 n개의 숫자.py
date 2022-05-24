def solution(x, n):
    answer = []
    i=0
    num=x
    while(i<n):
        answer.append(num)
        num+=x
        i+=1
    return answer

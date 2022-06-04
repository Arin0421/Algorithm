def solution(n):
    answer = 0
    li=[]
    while n>0:
        li.append(n%3)
        n=n//3
    print(len(li))
    for i in range(len(li)):
        answer+=li[i]*(3**(len(li)-1-i))
    return answer

def solution(n):
    answer = ''
    num=[]
    while n>0:
        num.append(n%10)
        n//=10
    num.sort(reverse=True)
    
    for i in num:
        answer+=str(i)
    return int(answer)

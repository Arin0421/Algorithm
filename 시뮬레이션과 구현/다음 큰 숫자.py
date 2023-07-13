def solution(n):
    num=bin(n).count('1')
    
    while True:
        n+=1
        temp=bin(n).count('1')
        if num==temp:
            break
    return n

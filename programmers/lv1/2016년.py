def solution(a, b):
    answer = ''
    week=["THU","FRI","SAT","SUN","MON","TUE","WED"]
    mon=[31,29,31,30,31,30,31,31,30,31,30,31]
    
    num=0
    for i in range(a-1):
        num+=mon[i]
    
    num+=b
    answer+=week[num%7]
    return answer

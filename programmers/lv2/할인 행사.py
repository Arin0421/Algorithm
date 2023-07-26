def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)-9):
        check=True
        for k in range(len(want)):
            if discount[i:i+10].count(want[k])!=number[k]:
                check=False
        if check:
            answer+=1
            
    return answer

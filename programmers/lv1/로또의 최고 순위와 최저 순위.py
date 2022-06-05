def solution(lottos, win_nums):
    answer = []
    min_re=0
    max_re=0
    
    for i in lottos:
        if i in win_nums:
            min_re+=1
            max_re+=1
        elif i==0:
            max_re+=1
    if max_re==6:
        answer.append(1)
    elif max_re==5:
        answer.append(2)
    elif max_re==4:
        answer.append(3)
    elif max_re==3:
        answer.append(4)
    elif max_re==2:
        answer.append(5)
    else:
        answer.append(6)
    if min_re==6:
        answer.append(1)
    elif min_re==5:
        answer.append(2)
    elif min_re==4:
        answer.append(3)
    elif min_re==3:
        answer.append(4)
    elif min_re==2:
        answer.append(5)
    else:
        answer.append(6)
    return answer

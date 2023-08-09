def solution(order):
    answer = 0
    tmp = []
    idx=1
    
    while idx != len(order)+1:
        tmp.append(idx)
        while tmp[-1] == order[answer]:
            answer += 1
            tmp.pop()
            if len(tmp) == 0:
                break
        idx += 1
    return answer

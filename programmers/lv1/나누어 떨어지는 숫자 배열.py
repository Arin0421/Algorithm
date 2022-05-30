def solution(arr, divisor):
    answer = []
    for data in arr:
        if data%divisor==0:
            answer.append(data)
    
    answer.sort()
    return answer if len(answer)!=0 else [-1]

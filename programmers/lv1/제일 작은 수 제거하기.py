def solution(arr):
    answer=[]
    for i in range(len(arr)):
        if arr[i]!=min(arr):
            answer.append(arr[i])
    if answer==[]:
        answer.append(-1)
    return answer

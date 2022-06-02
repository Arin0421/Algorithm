def solution(nums):
    num=len(nums)/2
    answer = 0
    li=[]
    for i in nums:
        if i not in li:
            li.append(i)
        if len(li)==num:
            break
    answer=len(li)
    return answer

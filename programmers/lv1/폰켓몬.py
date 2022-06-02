def solution(nums):
    li=[]
    for i in nums:
        if i not in li:
            li.append(i)
        if len(li)==len(nums)/2:
            break
    return len(li)

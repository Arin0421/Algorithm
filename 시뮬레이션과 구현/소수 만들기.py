import itertools
def solution(nums):
    answer = 0

    com=list(itertools.combinations(nums,3))
    
    for ele in com:
        num=sum(ele)
        check=0
        for i in range(2,num):
            if num%i==0:
                check=1
                break
        if check==0:
            answer+=1
    return answer


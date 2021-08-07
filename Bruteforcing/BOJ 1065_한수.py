num=int(input())
han=0

for n in range(1,num+1):
    if n<=99:
        han+=1

    else:
        nums=list(map(int,str(n))) #숫자를 자릿수대로 분리
        if nums[0] - nums[1] == nums[1]-nums[2]:
            han+=1


print(han)

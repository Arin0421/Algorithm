def solution(s):
    answer = []
    cnt=0
    zero_cnt=0
    while True:
        if s=='1':
            break
            
        temp=''
        for i in s:
            if i=='1':
                temp+=i
            else:
                zero_cnt+=1
        cnt+=1
        s=bin(len(temp))[2:]
        
    answer.append(cnt)
    answer.append(zero_cnt)
    return answer

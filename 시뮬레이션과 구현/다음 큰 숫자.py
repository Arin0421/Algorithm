def cnt_one(x):
    cnt=0
    for i in x:
        if i=='1':
            cnt+=1
    return cnt

def solution(n):
    answer = n
    while True:
        answer+=1
    
        n_temp=bin(n)[2:]
        ans_temp=bin(answer)[2:]
        
        n_one=cnt_one(n_temp)
        ans_one=cnt_one(ans_temp)
        
        if n_one==ans_one:
            break
    return answer

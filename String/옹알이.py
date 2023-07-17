def solution(babbling):
    answer = 0
    arr=["aya","ye","woo","ma"]
    
    for baby in babbling:
        cnt=0
        word=''
        for i in baby:
            word+=i
            if word in arr:
                word=''
                cnt+=1
        if len(word)==0 and cnt>0:
            answer+=1
            
    return answer

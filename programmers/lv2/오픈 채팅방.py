def solution(record):
    answer = []
    res=[]
    dic={}
    for i in range(len(record)):
        res.append(record[i].split())
        
    for i in range(len(record)):
        if res[i][0]!="Leave":
            dic[res[i][1]]=res[i][2]
    
    for i in range(len(record)):
        if res[i][0]=="Enter":
            answer.append(dic[res[i][1]]+"님이 들어왔습니다.")
        elif res[i][0]=="Leave":
            answer.append(dic[res[i][1]]+"님이 나갔습니다.")
    return answer

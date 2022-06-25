def solution(id_list, report, k):
    answer=[0]*len(id_list)
    ven={}
    user={}
    report=list(set(report))
    
    for i in id_list:
        ven[i]=0
        
    for i in report:
        a,b=i.split()
        
        if a not in user:
            user[a]=[b]
        else:
            user[a]+=[b]
        if b not in ven:
            ven[b]=1
        else:
            ven[b]+=1
            
    for r in report:
        a,b = r.split()
        if ven[b] >= k:
            answer[id_list.index(a)] += 1
    return answer

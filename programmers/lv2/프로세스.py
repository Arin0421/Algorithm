def solution(priorities, location):
    answer = 0
    
    while True:
        temp=priorities.pop(0)
        check=True
        if any(temp<i for i in priorities):
            priorities.append(temp)
            check=False
        
        if check:
            answer+=1
        
        if location==0 and check==True:
            break
            
        if location==0:
            location=len(priorities)-1
        else:
            location-=1
        
    return answer

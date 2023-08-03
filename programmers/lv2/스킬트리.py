def solution(skill, skill_trees):
    answer = 0
    
    s=list(skill)
    
    for skill_tree in skill_trees:
        temp=[]
        check=True
        for k in skill_tree:
            if k in s:
                temp.append(k)
                if s.index(k)!=len(temp)-1:
                    check=False
        if check:
            answer+=1
    return answer

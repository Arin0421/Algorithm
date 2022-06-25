def solution(s):
    answer = True
    temp=[]
    for i in s:
        if i=='(':
            temp.append(i)
        else:
            if len(temp)==0:
                return False
            else:
                temp.pop()
    if len(temp)==0:
        return True
    else:
        return False

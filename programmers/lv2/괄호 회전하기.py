def isRight(s):
    temp=[]
    for i in s:
        if len(temp)==0:
            temp.append(i)
        elif temp[-1]=='(' and i==')':
            temp.pop()
        elif temp[-1]=='[' and i==']':
            temp.pop()
        elif temp[-1]=='{' and i=='}':
            temp.pop()
        else:
            temp.append(i)
    
    if len(temp)==0:
        return True
    else:
        return False
    
def solution(s):
    answer = 0
    k=len(s)
    for i in range(len(s)):
        arr=[]
        arr=s[i:]+s[0:i]
        if isRight(arr):
            answer+=1
    return answer

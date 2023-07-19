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
    
    return (True if len(temp)==0 else False)
    
def solution(s):
    answer = 0
    k=len(s)
    for i in range(len(s)):
        if isRight(s):
            answer+=1
        s=s[1:]+s[0]
    return answer

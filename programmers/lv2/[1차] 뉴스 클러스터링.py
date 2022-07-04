def solution(str1, str2):
    answer = 0
    li1=jar(str1)
    li2=jar(str2)

    li1copy=li1.copy()
    li2copy=li2.copy()
    
    if len(li1)==0 and len(li2)==0:
        return 65536
    
    inter=[]
    for i in li1:
        if i in li2copy:
            inter.append(i)
            li1copy.remove(i)
            li2copy.remove(i)
            
    
    uni=len(li1copy)+len(li2copy)+len(inter)
    
    if uni!=0:
        answer=len(inter)/uni
        return int(answer*65536)
    
def jar(str):
    li=[]
    for i in range(len(str)-1):
        if str[i].isalpha() and str[i+1].isalpha():
            li.append((str[i].upper(),str[i+1].upper()))
    return li

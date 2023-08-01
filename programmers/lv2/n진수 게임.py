def jin(n,num):
    temp=''
    arr=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    if num==0:
        return '0'
    while num>0:
        temp=str(arr[num%n])+temp
        num//=n
    return temp

def solution(n, t, m, p):
    answer = ''
    arr=''
    for i in range(t*m):
        arr+=jin(n,i)
    
    while len(answer)<t:
        answer+=arr[p-1]
        p+=m
        
    return answer

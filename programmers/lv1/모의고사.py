def solution(answers):
    answer = []
    st1=[1,2,3,4,5]
    st2=[2,1,2,3,2,4,2,5]
    st3=[3,3,1,1,2,2,4,4,5,5]
    sol1,sol2,sol3=0,0,0
    
    for i in range(len(answers)):
        s1=i%5
        s2=i%8
        s3=i%10
        
        if st1[s1]==answers[i]:
            sol1+=1
        if st2[s2]==answers[i]:
            sol2+=1
        if st3[s3]==answers[i]:
            sol3+=1
        
    k=max(sol1,sol2,sol3)
    if k==sol1:
        answer.append(1)
    if k==sol2:
        answer.append(2)
    if k==sol3:
        answer.append(3)
    
    return answer

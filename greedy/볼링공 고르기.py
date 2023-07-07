n,m=map(int,input().split())
data=list(map(int,input().split()))

ans=0
for i in range(n):
    temp=[]
    temp.append(data[i])
    for j in range(i,n):
        if temp[-1]!=data[j]:
            ans+=1

print(ans)

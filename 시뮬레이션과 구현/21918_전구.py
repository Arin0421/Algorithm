n,m=map(int,input().split())
s=list(map(int,input().split()))

for _ in range(m):
    num,l,r=map(int,input().split())

    if num==1:
        s[l-1]=r
    elif num==2:
        for i in range(l,r+1):
            if s[i-1]==1:
                s[i-1]=0
            else:
                s[i-1]=1
    elif num==3:
        for i in range(l-1,r):
            s[i]=0
    else:
        for i in range(l-1,r):
            s[i]=1
for i in range(len(s)):
    print(s[i],end=' ')

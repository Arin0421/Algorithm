n=int(input())
ans=0

while n>1:
    if n%5==0:
        ans+=n//5
        n=n-5*(n//5)
    else:
        ans+=1
        n-=2

if ans==0 or n>=1:
    print(-1)
else:
    print(ans)

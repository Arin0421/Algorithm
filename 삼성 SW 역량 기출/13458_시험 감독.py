import sys
input=sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))
b,c=map(int,input().split())

ans=0
for i in range(n):
    data[i]-=b
    ans+=1
    if data[i]<=0:
        continue
    if data[i]%c==0:
        ans+=data[i]//c
    else:
        ans+= data[i]//c +1

print(ans)

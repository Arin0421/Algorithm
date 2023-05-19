import sys
input=sys.stdin.readline

n=int(input())
s=list(map(int,input().split()))
result=[1]*n

for i in range(1,n):
    for j in range(i):
        if s[j]<s[i]:
            result[i]=max(result[i],result[j]+1)
print(max(result))

ans=[]
order=max(result)
for i in range(n-1,-1,-1):
    if result[i]==order:
        ans.append(s[i])
        order-=1

ans.reverse()
print(*ans)

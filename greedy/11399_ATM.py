n=int(input())
lines=list(map(int,input().split()))

ans=0
lines.sort()
result=0

for i in lines:
    ans=ans+i
    result+=ans

print(result)

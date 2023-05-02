n=int(input())
tips=[]
ans=0

for _ in range(n):
    tips.append(int(input()))

tips.sort(reverse=True)

for i in range(len(tips)):
    if tips[i]-i>0:
        ans+=tips[i]-i

print(ans)

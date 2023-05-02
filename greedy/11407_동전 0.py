n,k=map(int,input().split())
coin=[]
ans=0

for _ in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in coin:
    if i<=k:
        ans+=k//i
        k=k-i*(k//i)

print(ans)

n=int(input())
drink=list(map(int,input().split()))

drink.sort()
k=drink.pop()

ans=sum(drink)/2+k
if ans%1==0:
    print(int(ans))
else:
    print(ans)

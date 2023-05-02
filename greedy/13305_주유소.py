n=int(input())
length=list(map(int,input().split()))
cities=list(map(int,input().split()))

ans=0
min_value=1e9

for i in range(len(length)):
    min_value=min(min_value,cities[i])
    ans+=length[i]*min_value

print(ans)

n=int(input())

cows={}

for i in range(1,11):
    cows[i]=-1

cnt=0
for _ in range(n):
    cow,location = map(int,input().split())
    if cows[cow]==-1:
        cows[cow]=location
    elif cows[cow]!=location:
        cnt+=1
        cows[cow]=location

print(cnt)

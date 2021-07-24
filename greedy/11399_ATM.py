N=int(input())

data=list(map(int,input().split()))

data.sort()

result=0
sum=0

for i in range(N):
    result=result+data[i]
    sum+=result
print(sum)

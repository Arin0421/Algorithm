n=int(input())
data=[]
ans=0
for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)

for i in range(n):
    if (i+1)%3!=0:
        ans+=data[i]

print(ans)

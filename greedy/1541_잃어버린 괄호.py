n=input()
arr=[]
arr=n.split('-')
ans=0

temp=arr[0].split('+')
for i in temp:
    ans+=int(i)

for i in range(1,len(arr)):
    temp=arr[i].split('+')
    num=0
    for i in temp:
        num+=int(i)
    ans-=num

print(ans)

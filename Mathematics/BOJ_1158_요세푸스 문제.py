n,k=map(int,input().split())

data=[]
for i in range(1,n+1):
    data.append(i)
result=[]
num=k-1

while len(data):
    if num>= len(data):
        num = num - len(data)
    else:
        result.append(str(data.pop(num)))
        num+=(k-1)

print("<",", ".join(result),">",sep="")

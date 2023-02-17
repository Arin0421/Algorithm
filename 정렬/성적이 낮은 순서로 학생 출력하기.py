n=int(input())
data=[]

for _ in range(n):
    a,b=map(str,input().split())
    data.append((a,int(b)))

data=sorted(data,key=lambda a:a[1])

for i in data:
    print(i[0],end=' ')

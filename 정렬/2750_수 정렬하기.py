n=int(input())
data=[]

for _ in range(n):
    k=int(input())
    data.append(k)

data.sort()

for i in range(n):
    print(data[i])
    

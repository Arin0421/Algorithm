n=input()
k=len(n)
result=[]

for i in range(k):
    result.append(n[i:k])

result.sort()

for i in range(len(result)):
    print(result[i])

n=int(input())
result=1
result2=0
for i in range(1,n+1):
    result*=i

data=''.join(reversed(str(result)))

for i in range(len(data)):
    if data[i]=='0':
        result2+=1
    else:
        break

print(result2)

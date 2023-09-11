n=int(input())
dic={}

for _ in range(n):
    a,b=input().split('.')
    if b not in dic:
        dic[b]=1
    else:
        dic[b]+=1

dic=sorted(dic.items())

for key,value in dic:
    print(key,value)

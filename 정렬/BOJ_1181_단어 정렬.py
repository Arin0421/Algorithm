n=int(input())
li=[]
for _ in range(n):
    a=input()
    if a not in li:
        li.append(a)

li.sort()
li.sort(key=len)
for data in li:
    print(data)

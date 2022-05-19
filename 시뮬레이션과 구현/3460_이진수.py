t=int(input())

for _ in range(t):
    li=[]
    n=int(input())

    while n>0:
        li.append(n%2)
        n=n//2

    for i in range(len(li)):
        if li[i]==1:
            print(i,end=' ')

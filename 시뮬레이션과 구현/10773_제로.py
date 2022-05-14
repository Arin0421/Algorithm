k=int(input())
li=[]
for i in range(k):
    comm=int(input())
    if comm==0:
        del li[-1]
    else:
        li.append(comm)

print(sum(li))

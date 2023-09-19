n=int(input())
res=[]

def back(idx):
    if idx==n:
        print(' '.join(map(str,res)))
        return

    for i in range(1,n+1):
        if i not in res:
            res.append(i)
            back(idx+1)
            res.pop()

back(0)

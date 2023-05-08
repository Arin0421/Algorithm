n,m=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
s=[]

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in data:
        if len(s)==0 or s[-1]<=i:
            s.append(i)
            dfs()
            s.pop()
dfs()

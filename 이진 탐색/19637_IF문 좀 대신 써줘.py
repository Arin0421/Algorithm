import sys
import bisect
input=sys.stdin.readline

n,m=map(int,input().split())

name=[]
value=[]
for i in range(n):
    a,b=map(str,input().split())
    name.append(a)
    value.append(int(b))

for _ in range(m):
    p=int(input())
    index=bisect.bisect_left(value,p)
    print(name[index])

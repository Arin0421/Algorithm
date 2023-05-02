n=int(input())
pt=list(map(int,input().split()))
pt.sort()
max_value=0

if n%2!=0:
    max_value = pt[-1]
    pt.pop()


for i in range(len(pt)//2+1):
    max_value=max(max_value,pt[i]+pt[-(i+1)])

print(max_value)

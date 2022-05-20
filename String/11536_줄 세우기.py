n=int(input())
li=[]

for _ in range(n):
    li.append(input())

incre_li = sorted(li)
decre_li = sorted(li,reverse=True)
if li == decre_li:
    print("DECREASING")
elif li == incre_li:
    print("INCREASING")
else:
    print("NEITHER")

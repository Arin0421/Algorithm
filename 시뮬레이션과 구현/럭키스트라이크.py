n=int(input())

num=str(n)
k=len(num)//2
left=0
right=0

for i in range(k):
    left+=int(num[i])
    right+=int(num[k+i])

if left==right:
    print("LUCKY")
else:
    print("READY")

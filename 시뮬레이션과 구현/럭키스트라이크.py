n=input()
length=len(n)
k=length//2

left=0
right=0

for i in range(k):
    left+=int(n[i])
    right+=int(n[length-i-1])

if left==right:
    print('LUCKY')
else:
    print('READY')

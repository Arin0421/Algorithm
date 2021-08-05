n=input()
length=len(n)
k=length//2

left_sum=0
right_sum=0

for i in range(k):
    left_sum+=int(n[i])
for j in range(k,length):
    right_sum+=int(n[j])

if left_sum == right_sum:
    print("LUCKY")
else:print("READY")
    

import sys
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

k=int(input())

for _ in range(k):
    arr=list(map(int,sys.stdin.readline().split()))
    total=0
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
            total+=gcd(arr[i],arr[j])
    print(total)

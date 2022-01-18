##
##m,n=map(int,input().split())
##nums=[]
##for i in range(m,n+1):
##    nums.append(i)
##    
##result=[]
##
##for i in nums:
##    cnt=0
##    if(i==1):
##        continue
##    for j in range(2,i+1):
##        if (i%j==0):
##            cnt+=1
##    if cnt==1:
##        result.append(i)
##
##for i in result:
##    print(i)

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)

import sys
input=sys.stdin.readline
data=input().rstrip()

max_val=''
min_val=''
m=0
for i in data:
    if i=='M':
        m+=1
    else:
        if m>0:
            max_val += str(5*(10**m))
            min_val += str(10**m + 5)
        else:
            max_val += '5'
            min_val += '5'
        m=0

if m>0:
    max_val+='1'*m
    min_val+=str(10**(m-1))

print(int(max_val))
print(int(min_val))

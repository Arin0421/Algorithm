import sys

while True:
    data=sys.stdin.readline().rstrip('\n')
    up,lo,sp,nu=0,0,0,0

    if not data:
        break
    for i in data:
        if i.isupper():
            up+=1
        elif i.islower():
            lo+=1
        elif i.isdigit():
            nu +=1
        elif i.isspace():
            sp+=1

    print(lo,up,nu,sp)

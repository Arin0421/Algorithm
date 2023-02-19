import sys


def cnt_odd(n):
    cnt=0
    for i in n:
        if int(i)%2==1:
            cnt+=1
    return cnt

def divide(n,cnt):
    global min_v, max_v
    s=str(n)
    cnt+=cnt_odd(s)

    if len(s)==1:
        min_v=min(min_v,cnt)
        max_v=max(max_v,cnt)
        return
    elif len(s)==2:
        divide(n//10+n%10,cnt)
    else:
        for i in range(1,len(s)-1):
            for j in range(i+1,len(s)):
                new_num=int(s[:i])+int(s[i:j])+int(s[j:])
                divide(new_num,cnt)

n=int(input())
min_v=float('inf')
max_v=0

divide(n,0)

print(min_v,max_v)

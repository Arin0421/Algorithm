import sys
input=sys.stdin.readline

t=int(input())

def back(idx,cnt):
    global ans
    if idx==11 and 0 not in position:
        ans=max(ans,cnt)
        return
    
    for i in range(11):
        if arr[idx][i] and position[i]==0:
            position[i]=1
            back(idx+1,cnt+arr[idx][i])
            position[i]=0

for _ in range(t):
    arr=[list(map(int,input().split())) for _ in range(11)]
    position=[0]*11

    ans=0
    back(0,0)
    print(ans)

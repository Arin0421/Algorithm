n=int(input())
eggs=[]

for _ in range(n):
    h,w=map(int,input().split())
    eggs.append([h,w])

answer=0
def cnt(eggs):
    global answer
    cnt=0
    for egg in eggs:
        if egg[0]<=0:
            cnt+=1
    answer=max(answer,cnt)

def egg(idx,eggs):
    global answer
    if idx==n:
        cnt(eggs)
        return

    if eggs[idx][0]<=0:
        egg(idx+1,eggs)
        return

    check=True
    for i in range(n):
        if idx==i:
            continue
        if eggs[i][0]>0:
            check=False
    if check:
        cnt(eggs)
        return

    for i in range(n):
        if i==idx:
            continue
        if eggs[i][0]<=0:
            continue
        eggs[idx][0]-=eggs[i][1]
        eggs[i][0]-=eggs[idx][1]
        egg(idx+1,eggs)
        eggs[idx][0]+=eggs[i][1]
        eggs[i][0]+=eggs[idx][1]

egg(0,eggs)
print(answer)

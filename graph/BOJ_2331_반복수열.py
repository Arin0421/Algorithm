a,p=map(int,input().split())

D=[0,a]


while True:
    tmp=0
    for s in str(D[-1]):
        tmp += int(s)**p

    if tmp in D:
        break
    D.append(tmp)

print(D.index(tmp)-1)

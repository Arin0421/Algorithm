import sys
input=sys.stdin.readline

n=int(input())

def dfs(enegram_dict,answer:list):
    if len(answer)==len(word):
        print("".join(answer))
        return

    for enegram in enegram_dict:
        if enegram_dict[enegram]:
            enegram_dict[enegram]-=1
            answer.append(enegram)
            dfs(enegram_dict,answer)
            enegram_dict[enegram]+=1
            answer.pop()

for _ in range(n):
    word=list(map(str,input().rstrip()))
    word.sort()
    enegram_dict=dict()
    for i in word:
        if i in enegram_dict.keys():
            enegram_dict[i]+=1
        else:
            enegram_dict[i]=1

    dfs(enegram_dict,[])

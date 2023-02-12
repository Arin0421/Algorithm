import sys
input=sys.stdin.readline

n=int(input())
num=list(map(int,input().split()))
op=list(map(int,input().split()))

min_result=10**7
max_result=-10**7
    
def dfs(i,result,add,sub,mul,div):
    global min_result,max_result
    if i==n:
        max_result=max(result,max_result)
        min_result=min(result,min_result)
        return

    if add:
        dfs(i+1,result+num[i],add-1,sub,mul,div)
    if sub:
        dfs(i+1,result-num[i],add,sub-1,mul,div)
    if mul:
        dfs(i+1,result*num[i],add,sub,mul-1,div)
    if div:
        dfs(i+1,int(result/num[i]),add,sub,mul,div-1)

dfs(1,num[0],op[0],op[1],op[2],op[3])
print(max_result)
print(min_result)

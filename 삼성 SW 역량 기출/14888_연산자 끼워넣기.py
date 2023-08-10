n=int(input())
arr=list(map(int,input().split()))
pl,mi,mul,div=map(int,input().split())

max_val=-int(1e9)
min_val=int(1e9)

def dfs(depth,val,pl,mi,mul,div):
    global min_val,max_val

    if depth==n:
        min_val=min(val,min_val)
        max_val=max(val,max_val)
        return

    if pl:
        dfs(depth+1,val+arr[depth],pl-1,mi,mul,div)
    if mi:
        dfs(depth+1,val-arr[depth],pl,mi-1,mul,div)
    if mul:
        dfs(depth+1,val*arr[depth],pl,mi,mul-1,div)
    if div:
        dfs(depth+1,int(val/arr[depth]),pl,mi,mul,div-1)


dfs(1,arr[0],pl,mi,mul,div)

print(max_val)
print(min_val)

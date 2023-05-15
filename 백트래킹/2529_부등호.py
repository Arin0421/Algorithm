from sys import stdin
input=stdin.readline

k=int(input())
sign=list(input().split())

visited=[0]*10
ans=[]

def check(i,j,k):
    if k=="<":
        return i<j
    else:
        return i>j

def dfs(depth,s):
    global max_ans, min_ans

    if(depth==k+1):
        ans.append(s)
        return

    for i in range(10):
        if not visited[i]:
            if(depth==0 or check(s[-1],str(i),sign[depth-1])):
                visited[i]=True
                dfs(depth+1,s+str(i))
                visited[i]=False

dfs(0,"")
print(max(ans))
print(min(ans))

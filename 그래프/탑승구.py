g=int(input())
p=int(input())
parent=[0]*(g+1)

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1,g+1):
    parent[i]=i

result=0
for i in range(p):
    data = find_parent(parent,int(input()))
    if data==0:
        break
    else:
        union_parent(parent,data,data-1)
        result+=1

plan=list(map(int,input().split()))
result=True

for i in range(m-1):
    if find_parent(parent,plan[i])!=find_parent(parent,plan[i+1])
        result=False

print(result)

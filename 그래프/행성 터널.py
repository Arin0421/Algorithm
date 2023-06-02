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

n=int(input())

parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

def cal_cost(x1,x2):
    result=abs(x1[0]-x2[0])
    for i in range(1,3):
        result=min(result,abs(x1[i]-x2[i]))
    return result
edges=[]
data=[]
for _ in range(n):
    x,y,z=map(int,input().split())
    data.append((x,y,z))

for i in range(n):
    for j in range(i,n):
        edges.append((cal_cost(data[i],data[j]),i+1,j+1))
edges.sort()

result=0
total=0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost

print(result)

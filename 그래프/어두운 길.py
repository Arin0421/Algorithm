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

n,m=map(int,input().split())

parent=[0]*n
for i in range(n):
    parent[i]=i

edges=[]
for _ in range(m):
    x,y,cost=map(int,input().split())
    edges.append((cost,x,y))

edges.sort()

result=0
total=0

for edge in edges:
    cost, a, b = edge
    total+=cost
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost

print(total - result)

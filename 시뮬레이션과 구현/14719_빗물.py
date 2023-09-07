h,w=map(int,input().split())
world=list(map(int,input().split()))

ans=0
for i in range(1,w-1):
    left=max(world[:i])
    right=max(world[i+1:])

    min_h=min(left,right)
    if world[i]< min_h:
        ans+=min_h - world[i]

print(ans)

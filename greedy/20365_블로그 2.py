n=int(input())
ps=input()

colors={'B':0, 'R':0}
colors[ps[0]]+=1

for i in range(1,n):
    if ps[i]!=ps[i-1]:
        colors[ps[i]]+=1

ans=min(colors['B'],colors['R'])
print(ans+1)

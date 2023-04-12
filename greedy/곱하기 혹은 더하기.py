s=input()
ans=0

for i in s:
    if ans==0:
        ans+=int(i)
    else:
        ans*=int(i)

print(ans)

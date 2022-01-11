n,k=map(int,input().split())

s=[ [0]*201 for i in range(201)]

for i in range(2,201):
    s[i][1]=1
for i in range(200):
    s[1][i+1]+=s[1][i]+1
for i in range(2,n+1):
    for j in range(2,k+1):
        s[i][j]=s[i][j-1]+s[i-1][j]
        
print(s[n][k]%1000000000)

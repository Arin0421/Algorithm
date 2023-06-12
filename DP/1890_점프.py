n=int(input())

graph=[ list(map(int,input().split())) for _ in range(n)]
data=[ [0]*n for _ in range(n)]
data[0][0]=1
for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:
            print(data[i][j])
            break
        val=graph[i][j]
        if i+val<n:
            data[i+val][j]+=data[i][j]
        if j+val<n:
            data[i][j+val]+=data[i][j]

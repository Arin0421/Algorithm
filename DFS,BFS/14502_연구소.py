import sys
from itertools import combinations
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int, input().split())) for _ in range(n)]
temp=[[0]*m for _ in range(n)]


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)

def get_area():
    area=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                area+=1
    return area


def dfs():
    result=0
    idxs=[]
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                idxs.append((i,j))
    for idx in list(combinations(idxs,3)):
        for i in idx:
            x,y=i
            graph[x][y]=1

        for i in range(n):
            for j in range(m):
                temp[i][j]=graph[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        result=max(result,get_area())

        for i in idx:
            x,y=i
            graph[x][y]=0

    return result
print(dfs())

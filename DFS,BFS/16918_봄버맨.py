from collections import deque
import sys
input=sys.stdin.readline

r,c,n=map(int,input().split())
graph=[list(map(str,input())) for _ in range(r)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def step1():
    for i in range(r):
        for j in range(c):
            if graph[i][j]=='O':
                q.append((i,j))

def step3():
    for i in range(r):
        for j in range(c):
            if graph[i][j]!='O':
                graph[i][j]='O'

def step4():
    while q:
        x, y = q.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                graph[nx][ny] = '.'
n-=1
while n:
    q = deque()

    step1()
    step3()

    n-=1
    if n==0:
        break
    step4()
    n-=1

for i in range(r):
    for j in range(c):
        print(graph[i][j],end='')
    print()

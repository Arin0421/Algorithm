import sys
input=sys.stdin.readline
data=[]

for _ in range(9):
    data.append(list(map(int,input().split())))

def checkRow(x, a):
    for i in range(9):
        if a == data[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == data[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == data[nx+i][ny+j]:
                return False
    return True

idxs=[]

for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            idxs.append([i, j])

def dfs(idx):

    if idx==len(idxs):
        for i in range(9):
            print(*data[i])
        exit(0)

    for i in range(1,10):
        x=idxs[idx][0]
        y=idxs[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            data[x][y] = i
            dfs(idx + 1)
            data[x][y] = 0

dfs(0)

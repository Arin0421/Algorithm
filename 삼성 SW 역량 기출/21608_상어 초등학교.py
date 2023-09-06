import sys
input=sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n ** 2)]
arr = [[0] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def find_like(info, x, y):
    cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            for j in info:
                if arr[nx][ny] == j and arr[nx][ny]!=0:
                    cnt += 1
    return cnt


def find_empty(info, x, y):
    cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 0:
                cnt += 1
    return cnt


for data in info:
    like_cnt, empty_cnt = 0, 0
    like_list = []
    for i in range(n):
        for j in range(n):
            num = data[0]
            like_cnt = find_like(data[1:], i, j)
            empty_cnt = find_empty(data[1:], i, j)
            like_list.append((like_cnt, empty_cnt, i, j))
    like_list = sorted(like_list, key=lambda x: (-x[0], -x[1], x[2], x[3]))
    for like_info in like_list:
        l_cnt,e_cnt,x,y=like_info
        if arr[x][y]==0:
            arr[x][y]=data[0]
            break

ans=0
score=[0,1,10,100,1000]

def find_idx(st):
    for i in range(n):
        for j in range(n):
            if arr[i][j]==st:
                return i,j
for k in info:
    temp=0
    x,y=find_idx(k[0])
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny] in k[1:]:
                temp+=1
    ans+=score[temp]

print(ans)

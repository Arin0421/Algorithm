import sys
from copy import deepcopy

n=int(input())
board=[]
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

def zero_up(board):
    for i in range(n-1):
        for j in range(n):
            if board[i][j]==0:
                board[i][j]=board[i+1][j]
                board[i+1][j]=0
    return board

def up(board):
    zero_up(board)
    for i in range(n):
        k = 0
        while k<n-1:
            if board[k][i] == board[k + 1][i]:
                board[k][i] *= 2
                board[k + 1][i] = 0
                k += 2
            else:
                k+=1
    zero_up(board)
    return board

def zero_down(board):
    for i in range(n-1,0,-1):
        for j in range(n):
            if board[i][j]==0:
                board[i][j]=board[i-1][j]
                board[i-1][j]=0
    return board

def down(board):
    zero_down(board)

    for i in range(n):
        k = n - 1
        while k>1:
            if board[k][i] == board[k - 1][i]:
                board[k][i] *= 2
                board[k - 1][i] = 0
                k -= 2
            else:
                k-=1
    zero_down(board)
    return board

def zero_left(board):
    for i in range(n):
        for j in range(n-1):
            if board[i][j]==0:
                board[i][j]=board[i][j+1]
                board[i][j+1]=0
    return board

def left(board):
    zero_left(board)
    for i in range(n):
        k = 0
        while k<n-1:
            if board[i][k] == board[i][k+1]:
                board[i][k] *= 2
                board[i][k+1] = 0
                k += 2
            else:
                k+=1
    zero_left(board)
    return board

def zero_right(board):
    for i in range(n):
        for j in range(n-1,0,-1):
            if board[i][j]==0:
                board[i][j]=board[i][j-1]
                board[i][j-1]=0
    return board

def right(board):
    zero_right(board)

    for i in range(n):
        k = n - 1
        while k>1:
            if board[i][k] == board[i][k-1]:
                board[i][k] *= 2
                board[i][k-1] = 0
                k -= 2
            else:
                k-=1
    zero_right(board)
    return board

ans=2

def run(board,dir):
    if dir==0:
        up(board)
    elif dir==1:
        left(board)
    elif dir==2:
        right(board)
    else:
        down(board)
    return board

def dfs(board,idx):
    global ans
    if idx==5:
        for i in range(n):
            for j in range(n):
                ans=max(ans,board[i][j])
        return

    for i in range(4):
        temp_board=run(deepcopy(board),i)
        dfs(temp_board,idx+1)

dfs(board,0)
print(ans)

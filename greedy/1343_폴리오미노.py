board=input()

for i in range(0,len(board)-3):
    if board[i:i+4]=='XXXX':
        board=board.replace('XXXX','AAAA')

for i in range(0,len(board)-1):
    if board[i:i+2]=='XX':
        board=board.replace('XX','BB')

if 'X' in board:
    print(-1)
else:
    print(board)

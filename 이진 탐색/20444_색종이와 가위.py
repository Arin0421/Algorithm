import sys
input=sys.stdin.readline

n,k=map(int,input().split())

row=0
col=n//2
isPosssible=False

while row<=col:
    rowCut=(row+col)//2
    colCut=n-rowCut

    pieces = (rowCut+1)*(colCut+1)

    if pieces==k:
        print('YES')
        isPosssible=True
        break
    if k>pieces:
        row=rowCut+1

    else:
        col=rowCut-1

if not isPosssible:
    print('NO')

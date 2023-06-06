from collections import deque
from sys import stdin
input = stdin.readline

w, h = map(int, input().split())
graph = [[0 for _ in range(w+2)] for _ in range(h+2)] # +2씩 해준다. 외밖과 닿는 면을 다 흰색정육각형으로 둘러준다.
for i in range(1, h+1):
    graph[i][1:w+1] = map(int, input().split())

dy = [0, 1, 1, 0, -1, -1]
dx = [[1, 0, -1, -1, -1, 0], [1, 1, 0, -1, 0, 1]] # 짝수줄, 홀수줄 범위내 이동거리 설정

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited = [[False for _ in range(w+2)] for _ in range(h+2)] # 방문체크 배열 생성
    visited[y][x] = True
    cnt = 0
    while queue:
        y, x = queue.popleft()

        for i in range(6):
            nx=x+dx[y%2][i]
            ny=y+dy[i]
            if 0<=ny<h+2 and 0<=nx<w+2:
                if graph[ny][nx]==0 and not visited[ny][nx]:
                    queue.append((ny,nx))
                    visited[ny][nx]=True
                elif graph[ny][nx]==1:
                    cnt+=1
    return cnt

print(bfs(0, 0))

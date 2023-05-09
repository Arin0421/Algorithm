import sys
input=sys.stdin.readline
n, m = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
count = 0


def dfs(x, y):
    global count
    if (x, y) == (1, m + 1):
        count += 1
        return

    if x == n:
        nx, ny = 1, y + 1
    else:
        nx, ny = x + 1, y

    dfs(nx, ny)

    if graph[x-1][y] == 0 or graph[x - 1][y - 1] == 0 or graph[x][y - 1] == 0:
        graph[x][y] = 1
        dfs(nx, ny)
        graph[x][y] = 0


dfs(1, 1)

print(count)

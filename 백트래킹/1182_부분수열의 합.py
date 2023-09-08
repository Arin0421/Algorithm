import sys
input=sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

def back(idx,temp):
    global ans

    if sum(temp) == s and len(temp) > 0:
        ans += 1

    for i in range(idx, n):
        temp.append(arr[i])
        back(i + 1,temp)
        temp.pop()


back(0,[])
print(ans)

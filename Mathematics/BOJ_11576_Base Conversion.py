x, y = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
ten = 0
answer =[]
for i in range(n):
    ten += a[-1] * (x**i)
    a.pop(-1)
while ten !=0:
    answer.append(str(ten % y))
    ten = ten // y

print(' '.join(answer[::-1]))

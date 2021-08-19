from sys import stdin
n=int(stdin.readline())
data=[]
for i in range(n):
    data.append(int(stdin.readline()))

data.sort()

for i in data:
    print(i)

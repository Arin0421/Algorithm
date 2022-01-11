import sys
n=int(sys.stdin.readline())
data=[0]*10001

for i in range(n):
    input_data=int(sys.stdin.readline())

    data[input_data]+= 1

for i in range(n):
    if data[i]!=0:
        for j in range(data[i]):
            print(i)
    


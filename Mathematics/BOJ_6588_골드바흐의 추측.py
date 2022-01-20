array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

import sys
input = sys.stdin.readline


while(True):                               
    n = int(input())

    if n==0 : break
    for i in range(3,n):
        if array[i] == True:
            if array[n-i] == True :
                print("%d = %d + %d"%(n , i , n-i))
                break
    else:
        print("Goldbach's conjecture is wrong.")

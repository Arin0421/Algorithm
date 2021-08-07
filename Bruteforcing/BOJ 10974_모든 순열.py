from itertools import permutations

n=int(input())
data=[i for i in range(1,n+1)]

for numbers in list(permutations(data)):
    for num in numbers:
        print(num,end=' ')
    print()

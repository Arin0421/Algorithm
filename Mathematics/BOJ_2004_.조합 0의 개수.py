import itertools
n,m=list(map(int,input().split()))
it = len(list(itertools.combinations(range(1,n),m)))

print(it)

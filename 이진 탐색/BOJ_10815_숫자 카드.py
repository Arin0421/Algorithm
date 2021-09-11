from sys import stdin
n=stdin.readline().rstrip()
array=list(map(int,stdin.readline().split()))
array.sort()
m=stdin.readline().rstrip()
target=list(map(int,stdin.readline().split()))

def binary(array, target, start, end):
    if start > end:
        return 0

    mid = (start + end) //2

    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary(array, target, start, mid-1)
    else:
        return binary(array, target, mid+1, end)

for num in target:
    start=0
    end=len(array)-1
    print(binary(array, num, start, end), end=' ')

import sys
input=sys.stdin.readline
n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        cnt = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                cnt += 1
                current = array[i]

        if cnt >= c:
            global result
            start = mid + 1
            result = mid
        else:
            end = mid - 1


start = 1
end = array[-1] - array[0]
result = 0

binary_search(array, start, end)
print(result)

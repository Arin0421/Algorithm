def binary_search(array, target, start, end):
    if start>end :
        return 0
    
    mid = (start + end) //2

    if array[mid] == target:
        return 1
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n=int(input())
array=list(map(int,input().split()))
array.sort()
m=int(input())
target=list(map(int,input().split()))

for num in target:
    start=0
    end = len(array)-1
    print(binary_search(array,num,start,end))

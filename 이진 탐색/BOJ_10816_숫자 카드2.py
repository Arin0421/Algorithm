from sys import stdin
def search(array, target, start, end):
    
    if start > end:
        return 0

    mid = (start + end) //2
    
    if array[mid] == target:
        return array[start:end+1].count(target)
    elif array[mid]>target:
        return search(array, target, start, mid-1)
    else:
        return search(array, target, mid+1, end)


n=stdin.readline().rstrip()
array=list(map(int,stdin.readline().split()))
array.sort()
m=stdin.readline().rstrip()
target=list(map(int,stdin.readline().split()))

n_dic={}
for num in array:
    start=0
    end=len(array)-1
    if num not in n_dic:
        n_dic[num]=search(array,num,start,end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in target))

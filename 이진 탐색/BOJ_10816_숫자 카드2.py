import sys
input=sys.stdin.readline

def binary_search(array, target, start, end):
    
    if start > end:
        return 0

    mid = (start + end) //2
    
    if array[mid] == target:
        return array[start:end+1].count(target)
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n=int(input())
n_list=list(map(int,input().split()))
n_list.sort()

m=int(input())
m_list=list(map(int,input().split()))

n_dic={}
for x in m_list:
    if x not in n_dic:
        n_dic[x]=binary_search(n_list,x,0,n-1)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in m_list))

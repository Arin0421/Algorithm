import heapq
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

arr.sort()

ans=[]
heapq.heappush(ans,arr[0][1])
for i in range(1,n):
    if arr[i][0] < ans[0]:
        heapq.heappush(ans,arr[i][1])
    else:
        heapq.heappop(ans)
        heapq.heappush(ans,arr[i][1])

print(len(ans))

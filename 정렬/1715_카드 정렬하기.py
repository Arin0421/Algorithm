import heapq

n=int(input())
card=[]

for _ in range(n):
    heapq.heappush(card,int(input()))

result=0

if len(card)==1:
    print(result)
else:
    while len(card)>1:
        min1=heapq.heappop(card)
        min2=heapq.heappop(card)
        result+=min1+min2
        heapq.heappush(card,min1+min2)

    print(result)

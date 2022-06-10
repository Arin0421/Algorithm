from collections import deque

def solution(prices):
    queue=deque(prices)
    answer = []
    while queue:
        sec=0
        price=queue.popleft()
        for i in queue:
            sec+=1
            if price>i:
                break
        answer.append(sec)
    return answer

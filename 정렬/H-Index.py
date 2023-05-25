def solution(citations):
    citations = sorted(citations)
    n = len(citations)
    
    for i in range(n):
        if citations[i] >= n-i:
            return n-i
    return 0

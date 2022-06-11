def solution(citations):
    n=len(citations)
    citations.sort()
    for i in range(n):
        h=citations[i]
        if n-i<=h:
            return n-i
    return 0

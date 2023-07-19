def solution(elements):
    result = set()
    
    k = len(elements)
    elements = elements * 2
    
    for i in range(k):
        for j in range(k):
            result.add(sum(elements[j:j+i+1]))
    return len(result)

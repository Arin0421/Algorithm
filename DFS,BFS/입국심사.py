def solution(n, times):
    answer = 0
    start=min(times)
    end=max(times)*n
    
    while start<=end:
        mid=(start+end)//2
        total=0
        for i in range(len(times)):
            total+=mid//times[i]
            
        if total>=n:
            end=mid-1
            answer=mid
        else:
            start=mid+1
            
    return answer

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
        
def solution(arr):
    answer = 1
    for i in range(len(arr)):
        answer=(answer*arr[i])/gcd(answer,arr[i])
    return answer


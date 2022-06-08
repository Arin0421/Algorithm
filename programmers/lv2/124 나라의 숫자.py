def solution(n):
    answer = ''
    n_arr=[1,2,4]
    while n>0:
        n=n-1
        answer = str(n_arr[n%3])+answer
        n//=3
    return answer

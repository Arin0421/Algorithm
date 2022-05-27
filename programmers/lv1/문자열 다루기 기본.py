def solution(s):
    answer = True
    str_len=len(s)
    if str_len!=4 and str_len!=6:
        return False
    for data in s:
        if data.isdigit()==0:
            return False
    return answer

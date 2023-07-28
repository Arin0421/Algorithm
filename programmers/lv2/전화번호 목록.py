def solution(phone_book):
    answer = True
    dic={}
    for phone_number in phone_book:
        dic[phone_number]=1
        
    for phone_number in phone_book:
        jub=''
        for num in phone_number:
            jub+=num
            if jub in dic and jub!=phone_number:
                return False
    return answer

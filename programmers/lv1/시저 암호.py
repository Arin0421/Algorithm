def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if 65<=ord(s[i])<=90:
            num=ord(s[i])+n
            if num>90:
                num-=26
            answer+=chr(num)
        elif 97<=ord(s[i])<=122:
            num=ord(s[i])+n
            if num>122:
                num-=26
            answer+=chr(num)
        else:
            answer+=' '
            
    return answer

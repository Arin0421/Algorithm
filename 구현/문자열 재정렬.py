s=input()

result=[]
value=0

for i in s:
    #알파벳인 경우 리스트에 삽입
    if i.isalpha():
        result.append(i)
    #숫자끼리 더하기
    else:
        value+=int(i)

result.sort()

if value!=0:
    result.append(str(value))

#최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))

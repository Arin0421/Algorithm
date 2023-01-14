s=input()

check=1
result=''
temp=''
for i in s:
    if i=='<':
        check*=-1
        result+=temp[::-1]
        temp=''
        result+=i
        continue
        
    elif i=='>':
        check*=-1
        result+=i
        continue
    elif i==' ':
        result+=temp[::-1]+' '
        temp=''
        continue

    if check==-1:
        result+=i
    else:
        temp+=i

result+=temp[::-1]

print(result)

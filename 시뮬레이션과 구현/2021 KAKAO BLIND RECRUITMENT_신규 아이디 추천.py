s=input()

answer=''

#1
s=s.lower()

#2
for i in s:
    if i.isalpha() or i.isdigit() or i in "-_.":
        answer+=i

#3
while '..' in answer:
    answer = answer.replace("..",".")

#4
if answer and answer[0] == '.':
    answer = answer[1:]
if answer and answer[-1] == '.':
    answer = answer[:-1]

#5
if answer=='':
    answer='a'

#6
if len(answer)>15:
    answer = answer[0:15]
    if answer[-1]==".":
        answer=answer[:-1]

#7
while len(answer) <3:
    answer+=answer[-1]

    
print(answer)

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

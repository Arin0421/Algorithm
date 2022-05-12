n=input()
list=[]
count=0

for i in n:
    if i.isalpha():
        list.append(i)
    else:
        count+=int(i)

list.sort()
if count != 0:
    list.append(str(count))

print(''.join(list))

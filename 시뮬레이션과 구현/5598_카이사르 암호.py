n=input()
result=[0]*len(n)
for i in range(len(n)):
    result[i]=ord(n[i])-3
    if result[i]<ord('A'):
        result[i]+=26
    result[i]=chr(result[i])
print(''.join(result))

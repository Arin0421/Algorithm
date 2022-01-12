import sys
s=list(sys.stdin.readline())
stack=[]
cnt=0

for i in range(len(s)-1):
    if s[i]=='(':
        stack.append('(')
        
    else:
        if s[i-1]=='(':
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1

            
print(cnt)


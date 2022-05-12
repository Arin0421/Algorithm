t = int(input())
stack = []

for _ in range(t):
    stack.clear()
    cnt = 0
    command = input()
    for i in command:
        if i == "(":
            stack.append(i)
        else:
            try:
                stack.pop()
            except:
                cnt = 1
                break
    if len(stack) == 0 and cnt == 0:
        print("YES")
    else:
        print("NO")

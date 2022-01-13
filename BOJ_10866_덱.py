import sys
n=int(sys.stdin.readline())
Deque=[]

for _ in range(n):
    cmd=sys.stdin.readline().split()

    if cmd[0]=='push_front':
        Deque.insert(0,cmd[1])
    elif cmd[0]=='push_back':
        Deque.append(cmd[1])
    elif cmd[0]=='pop_front':
        if len(Deque)==0:
            print(-1)
        else:
            print(Deque[0])
            del Deque[0]
    elif cmd[0]=='pop_back':
        if len(Deque)==0:
            print(-1)
        else:
            print(Deque.pop())
            
    elif cmd[0]=='size':
        print(len(Deque))
    elif cmd[0]=='empty':
        if len(Deque)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=='front':
        if len(Deque)==0:
            print(-1)
        else:
            print(Deque[0])
    elif cmd[0]=='back':
        if len(Deque)==0:
            print(-1)
        else:
            print(Deque[-1])
            

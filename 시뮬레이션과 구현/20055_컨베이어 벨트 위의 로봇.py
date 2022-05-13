from collections import deque

n,k=map(int,input().split())
belt=deque(map(int,input().split()))
robot=deque([0]*2*n)

level=1
while 1:
    belt.rotate(1)
    robot.rotate(1)
    robot[n-1]=0

    for i in range(n,-1,-1):
        if robot[i] and not robot[i+1] and belt[i+1]:
            belt[i+1]-=1
            robot[i+1], robot[i]=robot[i],0
    robot[n-1]=0
    if not robot[0] and belt[0]:
        robot[0]=1
        belt[0]-=1
    if belt.count(0)>=k:
        print(level)
        break
    level+=1

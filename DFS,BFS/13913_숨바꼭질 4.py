from collections import deque
n,k=map(int,input().split())
MAX=100001
visit=[0]*MAX
move=[0]*MAX

def path(x):
    arr=[]
    temp=x
    for _ in range(visit[x]+1):
        arr.append(temp)
        temp=move[temp]
    print(' '.join(map(str,arr[::-1])))

def bfs():
    q=deque([n])
    while q:
        v=q.popleft()
        if v==k:
            print(visit[v])
            path(v)
            return
        for next in (v-1,v+1,v*2):
            if 0<=next<MAX and not visit[next]:
                visit[next]=visit[v]+1
                q.append(next)
                move[next]=v

bfs()

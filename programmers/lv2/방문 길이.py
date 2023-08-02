def solution(dirs):
    visit = set()
    x,y = 0, 0
    cmd = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    
    for dir in dirs:
        dy, dx = cmd[dir]
        ny = y + dy
        nx = x + dx
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            visit.add(((x,y), (nx, ny)))
            visit.add(((nx, ny), (x, y)))
            x=nx
            y=ny
            
    return len(visit) // 2

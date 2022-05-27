def solution(s):
    answer = True
    p_cnt=0
    y_cnt=0
    
    for data in s:
        if data=='p' or data=='P':
            p_cnt+=1
        elif data=='y' or data=='Y':
            y_cnt+=1

    if p_cnt==y_cnt:
        return True
    else:
        return False

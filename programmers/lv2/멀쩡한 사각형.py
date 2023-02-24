def solution(w,h):
    answer = 0
    for x in range(1, w):
        if w == h:
            return w*h - w
        elif w == 1 or h == 1:
            return 0
        answer += int((h*x)/w)
    return answer * 2

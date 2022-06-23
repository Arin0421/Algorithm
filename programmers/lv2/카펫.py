def solution(brown, yellow):
    answer = []
    if yellow<4:
        brown-=4
        answer.append(yellow+2)
        answer.append(3)
    else:
        for i in range(int(yellow**0.5),0,-1):
            wid=(yellow//i)+2
            hei=i
            if yellow%i==0:
                if (wid+hei)*2==brown:
                    answer.append((yellow//i)+2)
                    answer.append(i+2)
                    break
                
    return answer

def solution(n, words):
    answer = []

    for i in range(len(words)):
        if words[i] in words[:i]:
            answer.append(i%n+1)
            answer.append((i//n)+1)
            break
        elif i>0 and words[i][0]!=words[i-1][-1]:
            answer.append((i%n)+1)
            answer.append((i//n)+1)
            break
    if len(answer)==0:
        answer.append(0)
        answer.append(0)
    return answer

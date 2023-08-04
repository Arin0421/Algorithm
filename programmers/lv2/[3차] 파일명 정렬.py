def solution(files):
    answer = []


    for file in files:
        head, number, tail = '', '', ''
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                for k in range(len(number)):
                    if not number[k].isdigit():
                        tail = number[k:]
                        number = number[:k]
                        break

                answer.append([head, number, tail])
                head, number, tail = '', '', ''
                break

    answer=sorted(answer,key=lambda x:(x[0].lower(),int(x[1])))
    return [''.join(i) for i in answer]

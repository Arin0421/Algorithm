code = {
    "063": 0,
    "010": 1,
    "093": 2,
    "079": 3,
    "106": 4,
    "103": 5,
    "119": 6,
    "011": 7,
    "127": 8,
    "107": 9,
}

get_key={v:k for k,v in code.items()}

def num(m):
    n = ""
    for i in range(0, len(m), 3):
        n += str(code[m[i : i + 3]])
    return int(n)

while True:
    n=input()
    if n=='BYE':
        break
    sp=n.split('+')
    a=sp[0]
    b=sp[1][:len(sp[1])-1]

    numA=num(a)
    numB=num(b)
    temp=str(numA+numB)

    result=''
    for i in temp:
        result+=get_key[int(i)]
    print(n+result)

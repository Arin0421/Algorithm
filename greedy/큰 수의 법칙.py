#N,M,k를 공백으로 구분하여 입력받기
n,m,k=map(int, input().split())
#n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, inpuut().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):#가장 큰 수를 k번 더하기
        if m==0:
            break
        result += first
        m-=1
    if m==0:
        break
    result+=second
    m-=1

print(result)

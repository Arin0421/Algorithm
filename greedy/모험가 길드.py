n=map(int,input())
data = list(map(int,input().split()))
data.sort()

result=0
count=0 #그룹에 속한 모험가의 수를 나타내기 위해 사
for i in data:
    count+=1
    if count>=i: #현재 그룹에 속한 모험가의 수가 현재 공포도 이상이라면 그룹 결성
        result+=1
        count=0 #그룹에 속한 모험가의 수 초기화

print(result)


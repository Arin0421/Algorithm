n=int(input())

data=[]
for _ in range(n):
    input_data=input().split()
    data.append((int(input_data[0]),input_data[1]))

data=sorted(data,key=lambda member:member[0])

for member in data:
    print(member[0],member[1])

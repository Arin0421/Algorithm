n=int(input())
ps=input()

blue=[]
red=[]

blue=ps.split('R')
red=ps.split('B')

blue_cnt=0
red_cnt=0

for i in blue:
    if 'B' in i:
        blue_cnt+=1

for i in red:
    if 'R' in i:
        red_cnt += 1

print(min(blue_cnt,red_cnt)+1)

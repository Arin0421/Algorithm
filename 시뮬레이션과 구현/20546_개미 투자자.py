n=int(input())
j,s=n,n
j_cnt,s_cnt=0,0

arr=list(map(int,input().split()))

for i in range(len(arr)):
    if j//arr[i]>0:
        temp=j//arr[i]
        j=j-(arr[i]*temp)
        j_cnt+=temp

up_cnt,dn_cnt=0,0

for i in range(1,len(arr)):
    if arr[i]>arr[i-1]:
        up_cnt+=1
        dn_cnt=0
    elif arr[i]<arr[i-1]:
        dn_cnt+=1
        up_cnt=0
    else:
        up_cnt=0
        dn_cnt=0

    if up_cnt==3 and s_cnt>0:
        temp=s//arr[i]
        s=s-(arr[i]*s//arr[i])
        s_cnt-=temp
    elif dn_cnt==3:
        temp=s//arr[i]
        s=s-(arr[i]*temp)
        s_cnt+=temp
    

j=j+arr[-1]*j_cnt
s=s+arr[-1]*s_cnt

if j>s:
    print("BNP")
elif s>j:
    print("TIMING")
else:
    print("SAMESAME")

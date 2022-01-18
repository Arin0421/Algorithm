##
##
##n=input()
##
##s=int(n,2)
##
##answer=''
##data="012345678"
##
##while s!=0:
##    answer+=str(data[s%8])
##    s//=8
##
##print(answer[::-1])


print(oct(int(input(),2))[2:])

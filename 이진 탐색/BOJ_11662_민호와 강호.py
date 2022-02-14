import sys
import math
input=sys.stdin.readline

x1,y1,x2,y2,x3,y3,x4,y4=map(float,input().split())

def minho(p):
    return [x1+(x2-x1)*(p/100),y1+(y2-y1)*(p/100)]

def kang(p):
    return [x3+(x4-x3)*(p/100),y3+(y4-y3)*(p/100)]

sp=0
ep=100


length =  math.sqrt(pow(10000, 2) + pow(10000, 2))

while (ep-sp>=1e-7):
    k1 = (sp*2 + ep)/3
    k2 = (sp + ep*2)/3
    m_k1 = minho(k1)
    m_k2 = minho(k2)
    k_k1 = kang(k1)
    k_k2 = kang(k2)

    dist_k1 = math.sqrt(pow(m_k1[0] - k_k1[0],2) + pow(m_k1[1] - k_k1[1],2))
    dist_k2 = math.sqrt(pow(m_k2[0] - k_k2[0],2) + pow(m_k2[1] - k_k2[1],2))

    length = min(length, min(dist_k1, dist_k2))
    
    if (dist_k1 >= dist_k2):
        sp=k1
    else:
        ep=k2

print('%.10f' %length)

import sys
input=sys.stdin.readline

n=int(input())

q=[0]*10001

for i in range(n):
    w=int(input())
    q[w]+=1

for i in range(1,10001):
    if q[i]!=0:
        for j in range(q[i]):
            print(i)

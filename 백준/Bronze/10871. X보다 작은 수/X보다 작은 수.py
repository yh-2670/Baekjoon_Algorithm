import sys
input=sys.stdin.readline

d=[]

a,b=map(int,input().split())
c=list(map(int,input().split()))

for i in range(a):
    if c[i]<b:
        d.append(c[i])
for j in range(len(d)):
    print(d[j], end=' ')
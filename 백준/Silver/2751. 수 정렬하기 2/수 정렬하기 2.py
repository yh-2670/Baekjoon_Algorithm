import sys
input= sys.stdin.readline

q=[]

n=int(input())

for i in range(n):
    a=int(input())
    q.append(a)

q.sort()

for i in range(n):
    print(q[i])
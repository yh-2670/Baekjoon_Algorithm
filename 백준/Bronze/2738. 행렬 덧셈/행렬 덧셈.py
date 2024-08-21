import sys
input = sys.stdin.readline
q=[]
w=[]
n,m=map(int,input().split())
for i in range(n):
    a=list(map(int,input().split()))
    q.append(a)
for j in range(n):
    b=list(map(int,input().split()))
    w.append(b)

for o in range(n):
    for p in range(m):
        print(q[o][p]+w[o][p], end=' ')
    print()
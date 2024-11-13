import sys
input=sys.stdin.readline

q=[]

n=int(input())

for i in range(n):
    order=list(input().split())
    if order[0]=='push':
        q.append(int(order[1]))
    if order[0]=='pop':
        if len(q)==0:
            print(-1)
        else:
            print(q[len(q)-1])
            q.pop()
    if order[0]=='size':
        print(len(q))
    if order[0]=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    if order[0]=='top':
        if len(q)==0:
            print(-1)
        else:
            print(q[len(q)-1])
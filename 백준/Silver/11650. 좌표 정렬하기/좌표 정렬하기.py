q=[]
n=int(input())

for i in range(n):
    m=list(map(int,input().split()))
    q.append(m)

q.sort()

for i in range(len(q)):
    print(*q[i])

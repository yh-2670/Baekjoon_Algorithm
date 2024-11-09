q=[]

n=int(input())

for i in range(n):
    v=list(map(int,input().split()))
    q.append(v)
q.sort(key=lambda x:(x[1],x[0]))

for i in range(n):
    print(q[i][0],q[i][1])
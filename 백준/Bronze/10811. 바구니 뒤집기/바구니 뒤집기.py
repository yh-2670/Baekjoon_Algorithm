n,m=map(int,input().split())
q=[]
for j in range(1,n+1):
    q.append(j)
for i in range(m):
    a,b=map(int,input().split())
    r=q[a-1:b]
    r.reverse()
    q[a-1:b]=r
print(*q)
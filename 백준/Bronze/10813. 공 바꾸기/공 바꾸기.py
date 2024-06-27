n,m=map(int,input().split())
l=[]
for j in range(1,n+1):
    l.append(j)
for i in range(m):
    a,b=map(int,input().split())
    l[a-1],l[b-1]=l[b-1],l[a-1]
print(*l)
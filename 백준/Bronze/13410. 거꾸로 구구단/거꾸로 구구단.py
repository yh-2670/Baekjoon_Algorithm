q=[]

n,m=map(int,input().split())
for i in range(1,m+1):
    a=str(n*i)
    q.append(int(a[::-1]))
print(max(q))
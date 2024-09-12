q=[]
n=int(input())
m=int(input())

for i in range(n,m+1):
    for j in range(0,i+1):
        if j*j==i:
            q.append(i)
if len(q)==0:
    print(-1)
else:
    print(sum(q))
    print(min(q))

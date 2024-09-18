q=[]
n,m=map(int,input().split())
for i in range(1,n+1):
    if n%i==0:
        q.append(i)
q.sort()
if len(q)<m:
    print(0)
else:
    print(q[m-1])
q=[]
n,m=map(int,input().split())
a=list(map(int,input().split()))

e=-100
for i in a:
    q.append(i)
    if len(q) == m:
        e=max(e,sum(q))
        q.pop(0)
print(e)

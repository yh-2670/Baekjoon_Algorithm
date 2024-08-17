a,b,c,d=map(int,input().split())

q=[]

for i in range(1,c+1):
    if c-a>=a:
        q.append(a)
    else:
        q.append(c-a)
    if d-b>=b:
        q.append(b)
    else:
        q.append(d-b)
print(min(q))
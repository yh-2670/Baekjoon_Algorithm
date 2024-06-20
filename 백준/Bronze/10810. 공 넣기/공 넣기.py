a,b=map(int,input().split())
l=[]
for j in range(a):
    l.append(0)
for i in range(b):
    c,d,e=map(int,input().split())
    for o in range(c-1,d):
        l[o]=e
print(*l)
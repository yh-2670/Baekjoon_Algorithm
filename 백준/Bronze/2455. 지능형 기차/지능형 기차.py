d=[]
c=0
for i in range(4):
    a,b=map(int,input().split())
    c=c-a
    d.append(c)
    c=c+b
    d.append(c)
print(max(d))
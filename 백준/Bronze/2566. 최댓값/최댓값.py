q=-1
r=0
c=0
for i in range(9):
    n=list(map(int,input().split()))
    if q>=max(n):
        q+=0
    elif q<max(n):
        q=max(n)
        r=i+1
        c=n.index(q) + 1
print(q)
print(r,c)
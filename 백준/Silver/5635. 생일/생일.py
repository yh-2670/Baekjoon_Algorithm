info=[]

n=int(input())

for i in range(n):
    n,d,m,y=input().split()
    d=int(d)
    m=int(m)
    y=int(y)
    info.append((y,m,d,n))
info.sort()

print(info[-1][3])
print(info[0][3])
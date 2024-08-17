q=0
a,b,c=map(int,input().split())

while True:
    if (a+b)<c:
        break
    w=0
    w=(a+b)//c
    q+=w
    o=(a+b)%c
    a=a-a+o+w
    b-=b
print(q)
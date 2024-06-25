a,b,c=map(int,input().split())
p=a*b

if (c-p)<0:
    print(p-c)
else:
    print(0)
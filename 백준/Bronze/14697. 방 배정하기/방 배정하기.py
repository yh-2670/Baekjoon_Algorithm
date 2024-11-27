a,b,c,n = map(int,input().split())

kkk=0

for i in range(50):
    for o in range(50):
        for k in range(50):
            if (a*i)+(b*o)+(c*k)==n:
                kkk=1
                break
if kkk==0:
    print(0)
else:
    print(1)
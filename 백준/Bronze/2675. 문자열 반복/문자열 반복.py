a=int(input())

for i in range(a):
    b,c=input().split()
    b=int(b)
    d=''
    for j in range(len(c)):
        d=d+c[j]*b
    print(d)
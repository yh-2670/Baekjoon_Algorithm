l=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())

e=0

if a%c==0:
    e=e+(a//c)
else:
    e=e+(a//c)+1

f=0

if b%d==0:
    f=f+(b//d)
else:
    f=f+(b//d)+1

if e>=f:
    print(l-e)
else:
    print(l-f)
a,b,c,d= map(int,input().split())
e=0
f=0

e= b//d
f= c//d

g= e*f

if g<=a:
    print(g)
else:
    print(a)
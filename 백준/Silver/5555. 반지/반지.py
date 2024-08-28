q=0
a=input()
b=int(input())
for i in range(b):
    n=input()
    m=n+n
    if a in m:
        q+=1
print(q)
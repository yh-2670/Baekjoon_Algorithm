b=[]
for i in range(10):
    a=int(input())
    a=a%42
    b.append(a)
    c=set(b)
print(len(c))
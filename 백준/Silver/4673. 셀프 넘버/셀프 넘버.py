l=[]
for i in range(1,10001):
    q=str(i)
    a=i
    for j in q:
        a+=int(j)
    l.append(a)

for i in range(1,10001):
    if i in l:
        continue
    else:
        print(i)
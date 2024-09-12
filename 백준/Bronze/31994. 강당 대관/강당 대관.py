q=[]
w=[]
for i in range(7):
    a,b=input().split()

    q.append(a)
    w.append(int(b))

p=w.index(max(w))

print(q[p])
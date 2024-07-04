w=0
q=[]
for i in range(4):
    a=int(input())
    q.append(a)
q.remove(min(q))

for o in range(3):
    w=w+q[o]

r=[]
for j in range(2):
    b=int(input())
    r.append(b)
r.remove(min(r))

w=w+min(r)

print(w)
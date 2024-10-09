q=[]

for i in range(9):
    n=int(input())
    q.append(n)
w=0
for j in range(8):
    if w==1:
        break
    for o in range(j+1,9):
        if sum(q)-q[j]-q[o]==100:
            q.remove(q[o])
            q.remove(q[j])
            w=1
            break
        else:
            continue
for i in q:
    print(i)
q=[]
n=input()

for i in n:
    q.append(int(i))

q.sort(reverse=True)

for i in range(len(q)):
    print(q[i],end='')

q=[]
qa=[]
final=0

n,nq,p = map(int,input().split())

for i in range(n):
    que=list(map(int,input().split()))
    q.append(que)

for i in range(p):
    qj,aj=map(int,input().split())
    qa.append([qj,aj])

hola=[0]*n
for i in range(n):
    for j in range(p):
        if q[i][qa[j][0]-1] == qa[j][1]:
            hola[i]+=1

for i in range(n):
    if hola[i]==p:
        final+=1

print(final)
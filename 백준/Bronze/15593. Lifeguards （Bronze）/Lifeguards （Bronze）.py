n=int(input())
work=[]
life=[0]*1000
for i in range(n):
    start,end=map(int,input().split())
    work.append((start, end))
    for j in range(start, end):
        life[j] += 1

res=0

for i in work:
    start, end = i[0], i[1]
    for j in range(start, end):
        life[j] -= 1
    time=0
    for k in life:
        if k>0:
            time+=1
    res=max(res,time)

    for q in range(start,end):
        life[q]+=1

print(res)
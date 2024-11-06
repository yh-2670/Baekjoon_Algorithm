number=[]
s=0

a,b=map(int,input().split())

start=1
for i in range(1,b+1):
    for j in range(start):
        number.append(start)
    start+=1

for i in range(a-1,b):
    s+=number[i]

print(s)

before=[]
after=[]

n=int(input())

b=input()
a=input()

for i in range(n):
    before.append(b[i])
    after.append(a[i])

count=0
flag=(-1)
for i in range(n):
    if before[i]!=after[i]:
        flag=1
    if before[i]==after[i] and flag==1:
        flag=(-1)
        count+=1
print(count)

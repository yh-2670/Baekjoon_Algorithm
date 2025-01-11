cow=[]
cnt=0

n=int(input())

for i in range(n):
    c=int(input())
    cow.append(c)

sortcow = sorted(cow)

if cow == sortcow:
    print(0)
else:
    for i in range(n):
        if cow[i] != sortcow[i]:
            cnt+=1
        
    print(cnt-1)
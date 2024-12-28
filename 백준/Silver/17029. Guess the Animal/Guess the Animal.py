n=int(input())
f=[[] for _ in range(n)]

for i in range(n):
    l=input().split()
    k=int(l[1])
    for j in range(2,len(l)):
        f[i].append(l[j])

maxcount=[]
for i in range(n):
    for j in range(i+1,n):
        count=0
        for a in f[i]:
            for b in f[j]:
                if a==b:
                    count+=1
        maxcount.append(count)

print(max(maxcount)+1)
            

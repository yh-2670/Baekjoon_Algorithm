total=0

n=int(input())

p=list(map(int,input().split()))

p.sort()

for i in range(n):
    for j in range(i+1):
        total+=p[j]

print(total)

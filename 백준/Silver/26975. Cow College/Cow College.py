final=[]

n=int(input())
want=list(map(int,input().split()))
want.sort()

howmuch=0
for j in range(n):
    percow=want[j]
    total=percow*(n-j)
    if total>howmuch:
        howmuch=total
        tuition=percow
    else:
        continue

print(howmuch,tuition)
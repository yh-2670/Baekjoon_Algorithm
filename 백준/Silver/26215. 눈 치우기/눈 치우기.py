import sys
input=sys.stdin.readline

total=0

n=int(input())

h=list(map(int,input().split()))

h.sort(reverse=True)

while True:
    if n==1:
        total+=h[0]
        break
    if h[0] > 0 and h[1] > 0:
        h[0] -= 1
        h[1] -= 1
        total+=1
        h.sort(reverse=True)
    elif h[0] > 0 and h[1] == 0:
        h[0] -= 1
        total+=1
    else:
        break
if total > 1440:
    print(-1)
else:
    print(total)
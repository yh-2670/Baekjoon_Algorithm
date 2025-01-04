import sys
input = sys.stdin.readline

n=int(input())
cow=[]

for i in range(n):
    loc, speed=map(int,input().split())
    cow.append(speed)

minn=cow[-1]
cnt=0

for i in range(n-2,-1,-1):
    if cow[i] > minn :
        continue
    else:
        cnt+=1

    minn=min(minn,cow[i])

print(cnt+1)
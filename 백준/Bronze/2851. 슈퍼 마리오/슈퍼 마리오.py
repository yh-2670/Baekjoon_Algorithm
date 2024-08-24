import sys
input = sys.stdin.readline

q=0

for i in range(10):
    n=int(input())
    r=q
    q+=n
    if q>=100:
        if abs(100-q)>abs(100-r):
            q=r
        break
print(q)
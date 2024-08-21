import sys
input = sys.stdin.readline

n=int(input())
a=n%100
if a>=49:
    print(n//100*100+99)
elif n<100:
    print(99)
else:
    print(n//100*100-1)
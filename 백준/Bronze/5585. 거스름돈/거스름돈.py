import sys
input = sys.stdin.readline

q=0
n=int(input())
a=1000-n
coins=[500,100,50,10,5,1]
for c in coins:
    q+=a//c
    a=a%c
print(q)

import sys
input=sys.stdin.readline


for i in range(3):
    n=int(input())
    a=0
    for j in range(n):
        m=int(input())
        a+=m
    if a==0:
        print(0)
    elif a>0:
        print("+")
    else:
        print("-")
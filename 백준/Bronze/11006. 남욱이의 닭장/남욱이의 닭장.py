n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=(b*2)-a
    d=b-c
    print(c,d)
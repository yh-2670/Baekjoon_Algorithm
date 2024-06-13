h,m=map(int,input().split())
t=int(input())

if m+t<=59:
    m=m+t
else:
    h=h+((t+m)//60)
    m=(m+t)%60
    if h>23:
        h=h-24
print(h,m)
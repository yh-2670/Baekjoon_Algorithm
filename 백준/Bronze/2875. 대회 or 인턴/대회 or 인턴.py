n,m,k=map(int,input().split())
a=0
while n>=2 and m>=1 and n+m-k>=3:
    a=a+1
    n=n-2
    m=m-1
print(a)
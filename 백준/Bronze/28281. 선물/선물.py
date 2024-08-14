b=[]
n,x=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n-1):
    b.append(a[i]*x+a[i+1]*x)
print(min(b))
a=list(map(int,input().split()))
b=0
for i in range(len(a)):
    b=b+a[i]**2
print(b%10)
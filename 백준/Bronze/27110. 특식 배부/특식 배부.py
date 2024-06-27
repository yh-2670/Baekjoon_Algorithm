m=int(input())
b=0
a=list(map(int,input().split()))

for i in range(len(a)):
    if m>=a[i]:
        b=b+a[i]
    else:
        b=b+m
print(b)
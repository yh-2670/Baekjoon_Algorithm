n=int(input())
a=list(map(int,input().split()))
b=(max(a))
c=0
for i in range(n):
    c=c+(a[i]/b*100)
print(c/n)
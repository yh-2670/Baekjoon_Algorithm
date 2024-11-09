n,k=map(int, input().split())
a=[]
for i in range(n):
    a.append(int(input()))
a.reverse()
total=0
num=0
for j in range(n):
    if k>=a[j]:
        num=k//a[j]
        k=k-a[j]*num

        total=total+num
print(total)

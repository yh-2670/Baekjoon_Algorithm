n=int(input())

for i in range(1,n+1):
    a=sum(map(int,str(i))) + i
    if a==n:
        print(i)
        break
    elif i==n:
        print(0)
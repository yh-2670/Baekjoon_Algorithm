n=int(input())

for i in range(n):
    q=[]
    b=0
    a=list(map(int,input().split()))
    for j in range(len(a)):
        if a[j]%2==0:
            q.append(a[j])
            b=b+a[j]
    print(b,min(q))
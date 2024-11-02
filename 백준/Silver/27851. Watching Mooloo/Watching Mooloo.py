n,k=map(int,input().split())

d=list(map(int,input().split()))

cost=0
for i in range(n):
    if i==0:
        cost=k+1
    else:
        fee=k+1
        diff=d[i]-d[i-1]
        cost+=min(fee,diff)

print(cost)
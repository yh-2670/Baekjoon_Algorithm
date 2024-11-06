t=int(input())

for i in range(t):
    bi=[]
    n=int(input())
    while n>0:
        if n%2==0:
            bi.append(0)
        else:
            bi.append(1)
        n=n//2
    for j in range(len(bi)):
        if bi[j]==1:
            print(j, end=' ')
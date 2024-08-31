q=0

n=int(input())
arr=[[0]*100 for i in range(100)]
for i in range(n):
    a,b=map(int,input().split())
    for j in range(a,a+10):
        for k in range(b,b+10):
            arr[j][k]=1
for l in range(100):
    for p in range(100):
        if arr[l][p] == 1:
            q+=1
print(q)
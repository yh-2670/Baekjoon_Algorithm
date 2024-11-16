count=0
n=int(input())
m=list(map(int,input().split()))

for i in range(n):
    if m[i]==1:
        continue
    else:
        for j in range(2,m[i]):
            if m[i]%j==0:
                break
        else:
            count+=1
       
print(count)
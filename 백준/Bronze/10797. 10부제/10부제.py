a= int(input())
b= list(map(int,input().split()))
c=0
for i in range(5):
    if b[i]==a:
        c=c+1
print(c)
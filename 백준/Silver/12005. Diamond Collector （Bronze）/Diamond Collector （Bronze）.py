maxcount=1
diamonds=[]

n,k=map(int,input().split())

for i in range(n):
    s=int(input())
    diamonds.append(s)
diamonds.sort()

for i in range(n):
    currentcount=1
    for j in range(i+1,n):
        if abs(diamonds[i]-diamonds[j])>k:
            break
        currentcount+=1
    if currentcount>maxcount:
        maxcount=currentcount

print(maxcount)
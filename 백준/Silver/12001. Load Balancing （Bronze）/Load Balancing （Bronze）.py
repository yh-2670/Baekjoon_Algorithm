cows=[]
res=10000000
n,b=map(int,input().split())

for i in range(n):
    cow=list(map(int,input().split()))
    cows.append(cow)
    
for j in range(n):
    for o in range(n):
        numm=0
        num1=0
        num2=0
        num3=0
        num4=0
        for p in range(n):
            if cows [p][0] > cows[j][0] +1 and cows[p][1] < cows[o][1]+1:
                num1+=1
            if cows[p][0] < cows[j][0] +1 and cows[p][1] < cows[o][1]+1:
                num2+=1
            if cows[p][0] > cows[j][0] +1 and cows[p][1] > cows[o][1]+1:
                num3+=1
            if cows[p][0] < cows[j][0] +1 and cows[p][1] > cows[o][1]+1:
                num4+=1

        numm=max(num1,num2,num3,num4)
        res=min(res,numm)
       
print(res)
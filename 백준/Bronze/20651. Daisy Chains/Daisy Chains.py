n=int(input())

num=list(map(int,input().split()))

count=0

for i in range(n):
    for j in range(i,n):
        summ=0
        if sum(num[i:j+1])/(len(num[i:j+1])) in num[i:j+1]:
                count+=1

print(count)
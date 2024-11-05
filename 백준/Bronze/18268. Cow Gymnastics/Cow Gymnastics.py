rank=[]

k,n=map(int,input().split())

for i in range(k):
    r=list(map(int,input().split()))
    rank.append(r)

count=0
res=0

for i in range(1,n+1):
    for j in range(i+1,n+1):
        count=0
        for a in range(k):
            if rank[a].index(i)>rank[a].index(j):
                count+=1
            else:
                count-=1
        if count==k or count==(-k):
            res+=1

print(res)

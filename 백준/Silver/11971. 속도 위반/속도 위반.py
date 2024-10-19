gap=0

tot1=[]
tot2=[]

n,m=map(int,input().split())

for i in range(n):
    dis, lim = map(int,input().split())
    for j in range(dis):
        tot1.append(lim)
        
for i in range(m):
    dist,speed = map(int,input().split())
    for j in range(dist):
        tot2.append(speed)

for i in range(100):
    gap=max(gap,tot2[i]-tot1[i])

print(gap)
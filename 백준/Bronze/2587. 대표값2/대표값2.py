n=[]
for i in range(5):
    q=int(input())
    n.append(q)
    
average=sum(n)//5
n.sort()
median=n[2]

print(average)
print(median)

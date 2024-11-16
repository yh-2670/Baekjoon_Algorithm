n,k=map(int,input().split())

number=[]
delete=[]

for i in range(2,n+1):
    number.append(i)

while number:
    standard=number[0]
    q=1
    while q * standard <= n:
        if q*standard in number:
            delete.append(q*standard)
            number.remove(q*standard)
        q+=1

print(delete[k-1])

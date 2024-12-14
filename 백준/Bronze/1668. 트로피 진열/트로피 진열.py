sang=[]
sang2=[]

n=int(input())

for i in range(n):
    q=int(input())
    sang.append(q)

for i in range(n):
    sang2.append(sang[n-i-1])
    
current=0
cnt=0

for i in sang:
    if i > current:
        cnt+=1
        current=i

current2=0
cnt2=0

for i in sang2:
    if i > current2:
        cnt2+=1
        current2=i

print(cnt)
print(cnt2)
t=0
y=0

n=list(map(int,input().split()))
q=min(n)

a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

t=sum(a)+sum(b)+sum(c)

for i in range(q):
    y+=max(a)*0.9+max(b)*0.9+max(c)*0.9
    a.remove(max(a))
    b.remove(max(b))
    c.remove(max(c))

print(t)
print(int(sum(a)+sum(b)+sum(c)+y))
q=[-1]*11
count=0

n=int(input())

for i in range(n):
    cow,cross=map(int,input().split())
    if q[cow] == (-1):
        q[cow]=cross
    elif q[cow]!=cross:
        count+=1
        q[cow]=cross

print(count)
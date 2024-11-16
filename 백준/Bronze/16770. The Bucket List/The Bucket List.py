milk=[0]*1001

n=int(input())

for i in range(n):
    s,t,b=map(int,input().split())
    for j in range(s,t+1):
        milk[j]+=b

print(max(milk))
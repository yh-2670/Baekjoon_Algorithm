m=int(input())
g=0
for i in range(m):
    a,b=map(int,input().split())
    if a==136:
        g=g+1000
    elif a==142:
        g=g+5000
    elif a==148:
        g=g+10000
    else:
        g=g+50000
print(g)

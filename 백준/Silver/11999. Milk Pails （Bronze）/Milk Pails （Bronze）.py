maxm=[]

x,y,m=map(int,input().split())

for i in range((m//x)+1):
    for j in range((m//y)+1):
        if (x*i)+(y*j) <= m:
            maxm.append((x*i)+(y*j))
        else:
            continue

print(max(maxm))
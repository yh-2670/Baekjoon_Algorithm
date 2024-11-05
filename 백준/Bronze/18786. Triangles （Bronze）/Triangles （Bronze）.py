final=[]

v=[]

n=int(input())

for i in range(n):
    q=list(map(int,input().split()))
    v.append(q)

for i in v:
    for j in v:
        for o in v:
            if i[0]==j[0] and j[1]==o[1]:
                final.append(abs(i[1]-j[1]) * abs(j[0]-o[0]))

print(max(final))

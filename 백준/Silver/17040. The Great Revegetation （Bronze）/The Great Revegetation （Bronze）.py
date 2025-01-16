n,m=map(int,input().split())

field = [1] * n

hola = []

for i in range(m):
    a,b=sorted(map(int,input().split()))
    hola.append([a-1,b-1])

hola.sort()

for i,j in hola:
    if field[i]==field[j]:
        field[j]+=1
    for q,w in hola [: hola.index([i,j])]:
        if field[q]==field[w]:
            field[j]+=1


print("".join(map(str, field)))


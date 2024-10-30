n=int(input())

location=list(map(int,input().split()))
for i in range(n):
    location[i]-=1

ID = list(map(int,input().split()))

for i in range(3):
    NEWID = ID.copy()
    for j in range(n):
        ID[j] = NEWID[location[j]]

for i in range(n):
    print(ID[i])
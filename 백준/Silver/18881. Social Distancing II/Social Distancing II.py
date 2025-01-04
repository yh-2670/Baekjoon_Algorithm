n = int(input())
cow = []
infected = []

for i in range(n):
    c = list(map(int, input().split()))
    cow.append(c)
   
cow.sort()
mindis = 1000000

for i in range(n):
    if cow[i][1] == 1:
        infected.append(cow[i][0])

for i in range(n):
    for j in range(n):
        if cow[i][1] == 0:
            if cow[j][1] == 1:
                dis = abs(cow[i][0] - cow[j][0])
                if dis != 0:
                    if mindis > dis:
                            mindis = dis
mindis -= 1

cnt = 1
for i in range(len(infected)-1):
    if infected[i]+mindis < infected[i+1]:
        cnt+=1

print(cnt)
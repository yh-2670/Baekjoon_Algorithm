from itertools import combinations

chong=[]

for i in range(9):
    n=int(input())
    chong.append(n)

for i in combinations(chong,7):
    k=list(map(int,i))
    if sum(k)==100:
        k.sort()
        for j in range(7):
            print(k[j])
        break
    else:
        pass
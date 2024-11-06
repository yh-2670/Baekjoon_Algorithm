from itertools import combinations

n,m=map(int,input().split())

q=[i for i in range(1,n+1)]

for i in combinations(q,m):
    print(*i)
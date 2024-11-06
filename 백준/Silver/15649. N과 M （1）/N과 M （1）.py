from itertools import permutations

n,m=map(int,input().split())
number=[i for i in range(1,n+1)]

for i in permutations(number,m):
    print(*i)

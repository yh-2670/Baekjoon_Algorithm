from itertools import permutations

odd=0
even=0

n=int(input())

num=list(map(int,input().split()))

for i in range(n):
    if num[i]%2==0:
        even+=1
    else:
        odd+=1

while odd-even >= 1:
    odd-=2
    even+=1

if odd < even:
    print(odd * 2 + 1)
else:
    print(odd+even)
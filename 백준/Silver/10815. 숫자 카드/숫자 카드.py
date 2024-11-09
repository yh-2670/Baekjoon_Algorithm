import sys
input=sys.stdin.readline

q=[]

n=int(input())
cardn=set(map(int,input().split()))

m=int(input())
cardm=list(map(int,input().split()))

for i in range(len(cardm)):
    if cardm[i] in cardn:
        q.append(1)
    elif cardm[i] not in cardn:
        q.append(0)

print(*q)

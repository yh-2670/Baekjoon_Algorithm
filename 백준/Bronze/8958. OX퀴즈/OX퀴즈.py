import sys
input=sys.stdin.readline

n=int(input())

for i in range(n):
    con=0
    score=0
    ox=list(input())
    for j in ox:
        if j=='O':
            con+=1
            score+=con
        else:
            con=0

    print(score)
    
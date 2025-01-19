import sys
input=sys.stdin.readline

n = int(input())

t = input()

c = list(map(int,input().split()))

ind = 0
res = 0
st = t[0]

howmany = t.count(st)

while st == t[ind] :
    if t[ind : c[ind]].count(st) != len(t[ind : c[ind]]):
        res+=1
    elif t[ind : c[ind]].count(st) == howmany :
        res+=1

    ind+=1

print(res)

import sys
input=sys.stdin.readline


n=int(input())
name=set()

for i in range(n):
    n,t=input().split()
    if n in name:
        name.remove(n)
    else:
        name.add(n)

name=sorted(name,reverse=True)

print(*name, sep = "\n")

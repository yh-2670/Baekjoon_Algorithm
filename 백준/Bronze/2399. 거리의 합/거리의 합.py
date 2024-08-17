import sys
input = sys.stdin.readline

n=int(input())
res=0
num=list(map(int,input().split()))
for i in range(len(num)):
    for j in range(len(num)):
        res=res+abs(num[i]-num[j])

print(res)
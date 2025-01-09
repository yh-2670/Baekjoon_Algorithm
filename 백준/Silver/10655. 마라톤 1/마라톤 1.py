import sys
input = sys.stdin.readline

n = int(input())
cp = []
s = 0
for i in range(n) :
    a, b = map(int, input().split())
    cp.append([a, b])
    
for i in range(n - 1) :
    s += abs(cp[i][0] - cp[i + 1][0])+abs(cp[i][1] - cp[i + 1][1])
minn = 10000000000
for i in range(n - 2) :
    q = abs(cp[i][0] - cp[i + 2][0]) + abs(cp[i][1] - cp[i + 2][1])
    total = abs(cp[i][0] - cp[i + 1][0]) + abs(cp[i][1] - cp[i + 1][1]) + abs(cp[i + 1][0] - cp[i + 2][0]) + abs(cp[i + 1][1] - cp[i + 2][1])
    
    minn = min(minn, s - total + q)
    
print(minn)
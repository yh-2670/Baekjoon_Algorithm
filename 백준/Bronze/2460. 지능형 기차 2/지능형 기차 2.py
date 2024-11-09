current=0
p=0

for i in range(10):
    a,b = map(int,input().split())
    current=(current-a)+b
    if current > p:
        p = current

print(p)

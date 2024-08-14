n=int(input())

for i in range(n):
    a=list(input().split())
    a.reverse()
    print("Case #"+str(i+1)+":",end=' ')
    print(*a)
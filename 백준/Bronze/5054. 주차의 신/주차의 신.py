t=int(input())

for i in range(t):
    n=int(input())
    shop=list(map(int,input().split()))
    print(2*(max(shop)-min(shop)))

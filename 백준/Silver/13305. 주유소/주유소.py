n=int(input())

road=list(map(int,input().split()))
price=list(map(int,input().split()))

oil=price[0]
pay=0
for i in range(len(road)):
    if price[i] < oil:
        oil = price[i]
    pay +=oil*road[i]

print(pay)
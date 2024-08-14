n=int(input())
for i in range(n):
    a=int(input())
    for i in range(a//5):
        print("++++", end=" ")
    print("|"*(a%5))
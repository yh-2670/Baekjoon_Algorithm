a,b,c=map(int,input().split())

li=[]
for i in range(a):
    n=input()
    li.append(n)

for i in li:
    for j in range(c):
        for k in i:
            print(k*c, end="")
        print()
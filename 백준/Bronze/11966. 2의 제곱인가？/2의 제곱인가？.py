a=[]
for i in range(31):
    a.append(2**i)

n=int(input())
if n in a:
    print(1)
else:
    print(0)
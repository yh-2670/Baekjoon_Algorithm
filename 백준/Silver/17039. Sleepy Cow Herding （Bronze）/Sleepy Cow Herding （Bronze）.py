cow=list(map(int,input().split()))

cow.sort()

if cow[0]+1==cow[1] and cow[1]+1==cow[2]:
    print(0)
elif cow[0]+2==cow[1] or cow[1]+2==cow[2]:
    print(1)
else:
    print(2)

if cow[2]-cow[1] >= cow[1]-cow[0]:
    print(cow[2]-cow[1]-1)
else:
    print(cow[1]-cow[0]-1)
from itertools import permutations
n = int(input())
l = []

for i in range(n) :
    cow = input().split()
    l.append((cow[0], cow[5]))
    
cows=["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]

cows.sort()

res = list((permutations(cows, 8)))
for i in res :
    check = True
    for j in range(n) :
        if abs(i.index(l[j][0]) - i.index(l[j][1])) == 1 :
            pass
        else :
            check = False
    if check == True :
        for k in range(len(cow)) :
            print(*i, sep = "\n")
            exit()
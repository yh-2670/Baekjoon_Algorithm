from itertools import permutations

n = int(input())
dice = []
for i in range(4) :
    d = input()
    dice.append(d)


    
for i in range(n) :
    s = input()
    q = list(permutations([0, 1, 2, 3], len(s)))
    canmake = False
    for j in q :
        ok = 0
        for k in range(len(s)) :
            if s[k] in dice[j[k]] :
                ok += 1
        if ok == len(s) :
            print("YES")
            canmake = True
            break
    if canmake == False:
        print("NO")
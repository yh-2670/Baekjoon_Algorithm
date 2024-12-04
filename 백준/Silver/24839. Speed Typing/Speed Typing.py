n=int(input())

for i in range(n):
    given=input()
    ba=input()

    gs=0
    for j in ba:
        if gs < len(given) and given[gs] == j :
            gs=gs+1
    if gs == len(given):
        print("Case #"+str(i+1)+": "+str(len(ba)-len(given)))
    else: print("Case #"+str(i+1)+": IMPOSSIBLE")
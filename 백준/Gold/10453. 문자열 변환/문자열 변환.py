n=int(input())

for i in range(n):
    aword=[]
    bword=[]
    a,b=input().split()
    for j in range(len(a)):
        if a[j] == "b":
            aword.append(j)
    for j in range(len(b)):
        if b[j] == "b":
            bword.append(j)

    if len(a) !=len(b):
        print(-1)
    else:
        cnt=0
        for o in range(len(aword)):
            cnt+=abs(bword[o] - aword[o])

        print(cnt)
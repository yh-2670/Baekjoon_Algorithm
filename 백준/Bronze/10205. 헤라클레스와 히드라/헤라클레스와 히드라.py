n=int(input())
for i in range(n):
    m=int(input())
    a=list(input())
    for o in range(len(a)):
        if a[o]=='c':
            m+=1
        elif a[o] == 'b':
            m-=1
        if m==0:
            break
    print("Data Set",i+1,end='')
    print(":")
    print(m)
    print()
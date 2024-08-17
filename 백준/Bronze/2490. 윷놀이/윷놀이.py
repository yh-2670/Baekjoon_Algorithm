for i in range(3):
    a,b,c,d=map(int,input().split())
    q=0
    if a==0:
        q+=1
    if b==0:
        q+=1
    if c==0:
        q+=1
    if d==0:
        q+=1
    if q==0:
        print("E")
    elif q==1:
        print("A")
    elif q==2:
        print("B")
    elif q==3:
        print("C")
    else:
        print("D")
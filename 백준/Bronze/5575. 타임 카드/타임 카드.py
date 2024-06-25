for i in range(3):
    h=0
    m=0
    s=0
    a,b,c,A,B,C=map(int,input().split())
    D=(A*3600)+(B*60)+C
    E=(a*3600)+(b*60)+c
    F=D-E
    h=F//3600%24
    m=(F//60)%60
    s=F%60
    print(h,m,s)
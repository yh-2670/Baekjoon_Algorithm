n=int(input())
q=0
for i in range(n):
    a,b,c,d,e=map(int,input().split())
    q=a*350.34 + b*230.90 + c*190.55 + d*125.30 + e*180.90
    print('$%.2f' % q)
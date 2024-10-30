import sys
input=sys.stdin.readline

n,m=map(int,input().split())
dis,dir =1,1
john=n
double=1
count=0

while True:
    for i in range(dis):
        john+=dir
        count+=1
        if john==m:
            print(count)
            exit()
    dir *= (-1)
    double*=2
    dis=abs(john-n)+double

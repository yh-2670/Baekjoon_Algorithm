import sys
input=sys.stdin.readline

xy = [[0]*1001 for i in range(1001)]
compare = [[0]*1001 for i in range(1001)]

n=int(input())

xx=[1,-1,0,0]
yy=[0,0,1,-1]

cnt=0

for i in range(n):
    x,y=map(int,input().split())
    if compare[x][y] == 3:
        cnt += 1
    xy[x][y]=1

    for j in range(4):
        newx = x + xx[j]
        newy = y + yy[j]

        if 0<= newx <= 1000 and 0<= newy <= 1000:
            compare[newx][newy] += 1
            if xy[newx][newy] :
                if compare[newx][newy] == 3 :
                    cnt += 1
                elif compare[newx][newy] == 4:
                    cnt-=1
    print(cnt)
x1, y1, x2, y2=map(int,input().split())
x3, y3, x4, y4=map(int,input().split())

if y3<=y1 and y2<=y4:
    if x3-x2<0 and x2-x4<0:
        x2=x3
    if x1-x4 < 0 and x3-x1<0:
        x1=x4
if x3<=x1 and x2<=x4:
    if y3-y2<0 and y2-y4<0:
        y2=y3
    if y1-y4 < 0 and y3-y1<0:
        y1=y4

print((x2-x1)*(y2-y1))
x11, y11, x21, y21=map(int,input().split())
x12, y12, x22, y22=map(int,input().split())

xmin = min(x11,x12)
xmax = max(x21,x22)
ymin = min(y11,y12)
ymax = max(y21,y22)

final = max(xmax-xmin,ymax-ymin)

print(final*final)

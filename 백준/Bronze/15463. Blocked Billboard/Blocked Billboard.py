count=0

x1, y1, x2, y2=map(int,input().split())
x3, y3, x4, y4=map(int,input().split())
x5, y5, x6, y6=map(int,input().split())

for i in range(-1000, 1001):
    for j in range(-1000, 1001):
        if x1<=i<x2 and y1<=j<y2:
            if x5<=i<x6 and y5<=j<y6:
                continue
            else:
                count+=1
                
        if x3<=i<x4 and y3<=j<y4:
            if x5<=i<x6 and y5<=j<y6:
                continue
            else:
                count+=1
print(count)
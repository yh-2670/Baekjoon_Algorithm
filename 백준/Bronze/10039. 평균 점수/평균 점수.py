a=[]
b=0
for i in range(5):
    a.append(int(input()))
    if a[i]<40:
        a[i]=40
    b=b+a[i]
print(b//(len(a)))
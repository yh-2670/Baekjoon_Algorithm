n=input()
b=0
for i in range(len(n)):
    if n[i]!=n[len(n)-(i+1)]:
        print('0')
        b=0
        break
    else:
        b=1
if b==1:
    print('1')
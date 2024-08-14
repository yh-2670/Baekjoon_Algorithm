n=int(input())
a=0
b=0
for i in range(n):
    m=input()
    if m=='D':
        a+=1
    elif m=='P':
        b+=1
    if a-2==b or b-2==a:
        break
print(str(a)+":"+str(b))
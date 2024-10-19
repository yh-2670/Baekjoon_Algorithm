a=0
b=1
n=int(input())
if n<=2:
    print(b)
else:
    for i in range(n-1):
        ans=a+b
        a=b
        b=ans
    print(ans)
n,m=map(int,input().split())
a=abs((m-1)//4-(n-1)//4)
b=abs((n-1)%4-(m-1)%4)
print(a+b)
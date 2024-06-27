a= int(input())

for i in range(1,a+1):
    print('*'*i+' '*((a*2)-(i*2))+'*'*i)
for j in range(1,a):
    print('*'*(a-j)+' '*(j*2)+'*'*(a-j))
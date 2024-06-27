a= int(input())

for i in range(1,a+1):
    print(' '*(a-i)+'*'*(i+(i-1)))
for j in range(1,a):
    print(' '*j+'*'*((a-j)+((a-1)-j)))
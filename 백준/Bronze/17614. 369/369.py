n=input()
q=0
for i in range(1, int(n)+1):
    q+=str(i).count('3')
    q+=str(i).count('6')
    q+=str(i).count('9')
print(q)